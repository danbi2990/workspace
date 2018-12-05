import re

raw_sites = """\
금융결제원(6) (giro.or.kr) 국민건강보험공단(5) (nhic.or.kr) 한국전력공사 (kepco.co.kr) 한국토지주택공사(4) (lh.or.kr) 금융감독원(7) (fss.or.kr) 한국관광공사(2) (visitkorea.or.kr) 근로복지공단(4) (kcomwel.or.kr) 한국산업인력공단(1) (hrdkorea.or.kr) 대한상공회의소(2) (korcham.net) 부산에듀넷(1) (busanedu.net) 경기도
민간분야100대사이트목록및ActiveX사용수
교육정보연구원 교 모네타(재테크포털)(2) 수학습지원센터 (moneta.co.kr)
(goedu.kr)
교통안전공 외환은행(6) (ts2020.kr) (keb.co.kr) 한국인터넷진흥원 비씨카드(3)
어바웃
(about.co.kr)
디앤샵(5) (dnshop.com) 이마트몰 (emartmall.com)
맥스무비(1) (maxmovie.com)
AK mall(8) (akmall.com)
(kisa.or.kr) (bccard.com) 서울특별시(1) 동양종합금융증권(6)
교수학습지원센터 (myasset.com) (ssem.or.kr)
맞춤형 복지포탈(2) 삼성화재(6) (gwp.or.kr) (samsungfire.com)
국립공원 관리공단(2) (knps.or.kr) 공무원연금공단(6) (geps.or.kr) 한국특허정보원 특 허정보검색서비스 (kipris.or.kr) 한국교육과정평가원(3) (kice.re.kr) 한국도로공사(5) (ex.co.kr)
금융(15)
KB국민은행(11) (kbstar.com) 신한카드(5) (shinhancard.com)
NH농협(9) (nonghyup.com)
우리은행(7) (wooribank.com)
신한은행(7) (shinhan.com)
삼성카드(5) (samsungcard.com)
현대카드(3) (hyundaicard.com) 롯데카드(3) (lottecard.co.kr) 하나은행(10) (hanabank.com) 기업은행(6) (ibk.co.kr)
포털(10)
네이버(1) (naver.com) 다음 (daum.net) 네이트(1) (nate.com) 야후!코리아(1) (yahoo.co.kr)
파란(8) (paran.com)
프리챌
(freechal.com)
드림위즈(5) (dreamwiz.com) 코리아닷컴 (korea.com) 천리안2.0(2) (chol.com) 세이클럽(2) (sayclub.com)
쇼핑(15)
옥션(10) (auction.co.kr0 G마켓(7) (gmarket.co.kr) 11번가(7) (11st.co.kr) 인터파크(6) (interpark.com) 롯데닷컴(6) (lotte.com) GS SHOP(2) (gsshop.com) CJmall(7) (cjmall.com) 신세계몰(6) (shinsegae.com) 롯데i몰(8) (lotteimall.com)
서점(10)
예스24(4) (yes24.com) 교보문고(4) (kyobobook.co.kr) 알라딘(1) (aladin.co.kr) 모아진(1) (moazine.co) 리브로(5) (libro.co.kr) 반디앤루니스(5) (bandinlunis.com) 개똥이네(5) (littlemom.co.kr) 영풍문고(7) (ypbooks.co.kr) 세원북(5) (swbook.co.kr) 북코아(5) www.bookoa.com
게임(10)
넥슨(4) (nexon.com) 한게임(10) (hangame.com) 피망(1) (pmang.com) 넷마블(12) (netmarble.net) 게임엔젤(2) (gameangel.com) 플레이엔씨(3) (plaync.co.kr) 디스이즈게임(1) (thisisgame.com) 인벤(3) (inven.co.kr) 게임트리(9) (gametree.co.kr) 윈디존(3) (windyzone.com)
기타(20)
조선닷컴(1) (chosun.com) 조인스MSN(1) (joinsmsn.com) 노컷뉴스(5) (nocutnews.co.kr) 마이데일리(1) (mydaily.co.kr) SBS (sbs.co.kr) MBN(1) (mbn.co.kr) 미투데이(1) (me2day.net) 티스토리 (tistory.com) Olleh-KT(2) (olleh.com)
T world(7) (tworld.co.kr)
티켓몬스터
(ticketmonster.co.kr)
쿠팡
(coupang.com)
사이트가드(1) (siteguard.co.kr)
다나와(2) (danawa.com)
메이크샵(1) (makeshop.co.kr) 잡코리아(2) (jobkorea.co.kr) 쉐어박스(3) (sharebox.co.kr)
멜론(2) (melon.com)
아프리카
(afreeca.com)
디시인사이드(5) (dcinside.com)
"""

grp_websites = re.findall(r'\(\D+?\)', raw_sites)
print(grp_websites)
print(len(grp_websites))

# remove_space = raw_sites.replace(" ", "\n")
# print(remove_space)

