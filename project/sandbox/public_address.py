
# from newslab_function.public_portal import get_df_from_url, save_tsv_from_df

import requests

# url = 'http://openapi.epost.go.kr/postal/retrieveNewAdressAreaCdService/retrieveNewAdressAreaCdService/getNewAddressListAreaCd?_wadl&type=xml?'

# url = url + 'serviceKey=Uk%2BJVYOgv9i2LwnIPLA6fz%2Fpv0NThtRf%2BZzSgFMi1Be1HMejVowag4ZZkwHTrCg7m3N2%2Byds8%2B8LMb76XPKUgw%3D%3D'

# url = url + '&srchwrd=주월동%20408-1'

# url = url + '&countPerPage=10'

# url = url + '&currentPage=1'

url = 'http://openapi.epost.go.kr/postal/retrieveNewAdressAreaCdService/retrieveNewAdressAreaCdService/getNewAddressListAreaCd?serviceKey=Uk%2BJVYOgv9i2LwnIPLA6fz%2Fpv0NThtRf%2BZzSgFMi1Be1HMejVowag4ZZkwHTrCg7m3N2%2Byds8%2B8LMb76XPKUgw%3D%3D&searchSe=dong&srchwrd=%EC%A3%BC%EC%9B%94%EB%8F%99%20408-1&countPerPage=10&currentPage=1'
print(url)

response = requests.get(url)
print(response.text)
