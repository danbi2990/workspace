import re

raw_sites = """
http://www.president.go.kr/ https://www.mma.go.kr/index.do      https://www.epeople.go.kr/jsp/user/UserMain.jsp http://www.neis.go.kr/
https://www.nis.go.kr:4016/main.do  http://www.dapa.go.kr/  https://www.hometax.go.kr/  http://www.share.go.kr/ https://www.schoolinfo.go.kr/
http://www.bai.go.kr/   https://www.mois.go.kr/ https://www.wetax.go.kr/    http://www.minwon.go.kr/main?a=AA020InfoMainApp http://oneclick.moe.go.kr/pas_ocl_mn00_001.do
https://kcc.go.kr/user.do   http://www.police.go.kr/main.html   http://www.work.go.kr/  https://www.consumer.go.kr/consumer/index.do    https://www.korean.go.kr/
    https://www.nfa.go.kr/nfa/  http://hrd.go.kr/hrdp/ma/pmmao/index.do http://www.ecar.go.kr/  http://www.nature.go.kr/
http://www.opm.go.kr/opm/index.do   https://www.mcst.go.kr/ https://job.mpva.go.kr/ http://epost.go.kr/ http://www.heritage.go.kr/
    http://www.cha.go.kr/main.html  https://gosi.kr/    http://www.law.go.kr/   http://www.culture.go.kr/
http://www.moleg.go.kr/ http://www.mafra.go.kr/ http://rt.molit.go.kr/  http://www.juso.go.kr/  https://www.tour.go.kr/
https://www.mpva.go.kr/ http://www.rda.go.kr/main/mainPage.do   http://luris.molit.go.kr/   https://www.foodsafetykorea.go.kr/  http://www.foreston.go.kr/
http://www.ftc.go.kr/   http://www.forest.go.kr/    https://seereal.lh.or.kr/main.do    http://www.gir.go.kr/   http://www.riverguide.go.kr/kor/index.do
http://www.fsc.go.kr/       http://www.alio.go.kr/  http://www.its.go.kr/   https://www.0404.go.kr/
http://www.acrc.go.kr/  http://www.smba.go.kr/  http://www.g4b.go.kr/       http://www.nl.go.kr/
http://www.moef.go.kr/  http://www.kipo.go.kr/  http://www.bizinfo.go.kr/   https://www.hikorea.go.kr/  https://www.museum.go.kr/
https://www.nts.go.kr/  http://www.mohw.go.kr/react/index.jsp   https://www.k-startup.go.kr/    https://www.privacy.go.kr/  http://www.korea.kr/
http://www.customs.go.kr/   http://mfds.go.kr/index.do      https://www.nanumkorea.go.kr/   https://www.gov.kr/portal/main
https://www.pps.go.kr/  http://www.me.go.kr/home/web/main.do    https://www.ei.go.kr/ei/eih/cm/hm/main.do   http://bokjiro.go.kr/nwel/bokjiroMain.do    http://kosis.kr/index/index.do
http://kostat.go.kr/portal/korea/index.action   http://www.kma.go.kr/   http://www.g2b.go.kr/   http://www.childcare.go.kr/ http://www.index.go.kr/
http://moe.go.kr/main.do    http://www.moel.go.kr/  http://www.d2b.go.kr/index.do   https://www.w4c.go.kr/
http://www.mofa.go.kr/www/index.do  http://www.mogef.go.kr/ http://www.patent.go.kr/portal/Main.do
http://www.unikorea.go.kr/      http://www.fta.go.kr/
http://www.moj.go.kr/HP/MOJ03/index.do  http://www.kcg.go.kr/
http://www.spo.go.kr/   http://www.naacc.go.kr/ http://www.kics.go.kr/
http://www.mnd.go.kr/mbshome/mbs/mnd/index.jsp  https://www.giro.or.kr/index.giro
https://msit.go.kr/web/main/main.do http://www.motie.go.kr/www/main.do  http://www.ecar.go.kr/Index.jsp http://www.car365.go.kr/    """

# grp_websites = re.findall(r'\(\D+?\)', raw_sites)
# print(grp_websites)
# print(len(grp_websites))

# remove_space = raw_sites.replace(" ", "\n")

split_return = raw_sites.split('\n')
# print(split_return)

split_space_raw = []
[split_space_raw.extend(line.split(' ')) for line in split_return]

split_space = list(filter(lambda x: x != '', split_space_raw))
print(split_space)
print(len(split_space))

# split_space = list(filter(lambda x: x != '', raw_sites.split(' ')))
# print(split_space)
# print(len(split_space))


















