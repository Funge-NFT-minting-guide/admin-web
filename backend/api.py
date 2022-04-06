import json

import pytz
from bson import json_util
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask, request, abort
from dateutil import parser as dateparser
from flask_restx import Api, Resource, fields, reqparse

from common import *
from db_connect import DAO

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
api = Api(app=app, version='1.0', title='Twitty-API')


minting_info = api.model('MintingInfo', {
    '_id': fields.String(readonly=True),
    'tweetId': fields.String(readonly=True),
    'profileImageUrl': fields.String(),
    'followers': fields.Integer(),
    'url': fields.String(),
    'projectName': fields.String(),
    'date': fields.Date(),
    'detail': fields.List,
    'site': fields.String(),
    'etc': fields.String(),
    })

parser = reqparse.RequestParser()
parser.add_argument('filter', type=str, choices=('_id', 'tweetId'))

db = DAO('funge-admin')

@api.route('/minting/info')
class MintingInfo(Resource):
    @api.marshal_list_with(minting_info)
    def get(self):
        ret = list(db.find('mintingInfo', {}))
        return ret


    def post(self):
        document = json.loads(request.data)
        print(document)
        object_id = document['objectId']
        print(object_id)
        del document['objectId']
        document['date'] = dateparser.parse(document['date']).astimezone(pytz.timezone('Asia/Seoul'))
        if not object_id:
            db.replace_one('mintingInfo', {'_id': ObjectId(object_id)}, document)
        else:
            db.insert_one('mintingInfo', document)
        return SUC_CREATED


@api.route('/minting/info/<string:_id>')
class MintingInfoTid(Resource):
    def get(self, _id):
        args = parser.parse_args()
        print(args)
        if args['filter'] == '_id':
            if _id != 'null':
                ret = list(db.find('mintingInfo', {args['filter']: ObjectId(_id)}))
            else:
                return abort(*ERR_NOT_FOUND)
        if args['filter'] == 'tweetId':
            ret = list(db.find('mintingInfo', {args['filter']: _id}))
        ret = [json.loads(json_util.dumps(x)) for x in ret]
        return ret if ret else abort(*ERR_NOT_FOUND)




if __name__ == '__main__':
    app.run(debug=True, host=SERVICE_HOST, port=SERVICE_PORT)
