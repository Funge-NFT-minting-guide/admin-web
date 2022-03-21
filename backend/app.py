from flask import Flask, jsonify


app = Flask(__name__)



@app.route('/api/minting')
def minting():
    return jsonify([{"_id":{"$oid":"622c2735cf057dee239dd167"},"id":"1502507922550824963","created_at":{"$date":"2022-03-12T04:52:58Z"},"text":"👹Raving Goblins 민팅 스케쥴!!👹\n03.12 (토요일) 오늘!!  ✅\n\n1회차  :  21:00 ~ 22:00  /  2차 화이트리스트 당첨자 대상\n(경쟁화리, 한번에 3고블린씩 지속 민팅 가능)\n💰 130 Klay\n\n2회차 :  23:00 ~ 24:00 / 퍼블릭 민팅\n(총 수량 잔여수량에 따름)\n💰 170 Klay","user":"📀 𝘋𝘚𝘊 𝘓𝘈𝘉𝘌𝘓","uid":"1389243389363724290","profile_image_url":"https://pbs.twimg.com/profile_images/1471812322041954305/xq0vnWgV_normal.jpg","followers":15819}, {"_id":{"$oid":"622b37f6670febd4fe8927a6"},"id":"1500739188781551616","created_at":{"$date":"2022-03-07T07:44:39Z"},"user":"4PAR DAO","uid":"1482740635115618305","profile_image_url":"http://pbs.twimg.com/profile_images/1483680165448552453/zJuCrIh5_normal.jpg","text":"[[4PAR DAO 민팅일정]]\n\n2차 민팅 (1st whitelist) : 3/24 오후 21:00~22:00시\n- 자격 : OG + wl1\n- 가격 : 350klay\n- 수량 : 3000개\n-트젝당 최대 2장 민팅 가능\n\n* Sold out 될 경우 화이트리스트이더라도 구매 실패. 이 경우 3차 민팅 (2nd whitelist)에서 도전 가능","followers":1370,"url":"https://twitter.com/4PARDAO/status/1500739188781551616"}, {"_id":{"$oid":"622b37f6670febd4fe8927a5"},"id":"1501196135335350274","created_at":{"$date":"2022-03-08T14:00:24Z"},"user":"Project Acies NFT","uid":"1491601625462763521","profile_image_url":"http://pbs.twimg.com/profile_images/1491608801728172034/Z4_Dqija_normal.jpg","text":"🎊민팅 시간 및 정보🎊\n날짜 : 3월 11일 19:00 ~ 13 일 19:00\n가격 : 200 Klay\n개수 : 9900 개 \n\n- 민팅 완료 후 약 한 달 후에 Reveal \n- 레이리티 종류 : 4등급( 일반, 희귀, 영웅, 전설)\n- 민팅 날 민팅 사이트 트위터/텔레그램에 공지\n- 완판되지 않을 경우 남은 NFT 소각\n\n많은 참여 부탁드립니다♥","followers":2310,"url":"https://twitter.com/AciesProject/status/1501196135335350274"}])

if __name__ == '__main__':
    app.run(debug=True)
