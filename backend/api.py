import json

import pytz
import datetime
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

faq = api.model('FAQ', {
    '_id': fields.String(),
    'question': fields.String(),
    'answer': fields.String(),
    })

parser = reqparse.RequestParser()
parser.add_argument('filter', type=str, choices=('_id', 'tweetId'))
parser.add_argument('query', type=str, default='{}')
parser.add_argument('startdate', type=str)
parser.add_argument('enddate', type=str)
parser.add_argument('offset', type=int)

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
        print(document['date'])
        if object_id:
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
            print(args['filter'])
            if _id != 'null':
                ret = list(db.find('mintingInfo', {args['filter']: ObjectId(_id)}))
            else:
                return abort(*ERR_NOT_FOUND)
        if args['filter'] == 'tweetId':
            ret = list(db.find('mintingInfo', {args['filter']: _id}))
        ret = [json.loads(json_util.dumps(x)) for x in ret]
        return ret if ret else abort(*ERR_NOT_FOUND)


@api.route('/minting/info/total')
class MintingInfoTotal(Resource):
    def get(self):
        ret = db.countTotal('mintingInfo')
        return ret


@api.route('/minting/info/total/date')
class MintingInfoToday(Resource):
    def get(self):
        args = parser.parse_args()
        ret = db.count('mintingInfo', {'date': {'$gte': datetime.datetime.strptime(args['startdate'], '%Y-%m-%d'), '$lt': datetime.datetime.strptime(args['enddate'], '%Y-%m-%d')}})
        return ret


@api.route('/tips/faq')
class FAQ(Resource):
    @api.marshal_list_with(faq)
    def get(self):
        args = parser.parse_args()
        ret = list(db.find('faq', {}).skip(args['offset']))
        return ret

    def post(self):
        faq = json.loads(request.get_data())

        ret = db.insert_one('faq', {'question': faq['question'], 'answer': faq['answer']})
        return SUC_CREATED if ret.acknowledged else abort(500, 'Something is wrong.')

    @api.marshal_with(faq)
    def put(self):
        faq = json.loads(request.get_data())

        ret = db.find_one_and_update('faq', {'_id': ObjectId(faq['_id'])}, {'$set': {'question': faq['question'], 'answer': faq['answer']}})
        return ret


@api.route('/tips/faq/<string:_id>')
class DeleteFAQ(Resource):
    def delete(self, _id):
        ret = db.delete_one('faq', {'_id': ObjectId(_id)})

        return SUC_DELETED if ret.acknowledged else abort(500, 'Something is wrong.')


if __name__ == '__main__':
    app.run(debug=True, host=SERVICE_HOST, port=SERVICE_PORT)
