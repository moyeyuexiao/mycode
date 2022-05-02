import requests

url = "https://www.google.com/recaptcha/api2/payload?p=06AGdBq24rpTCwSP4HK2lo_f72CSF8KFalWGKzexouVN4dNocxOmmxB_LKF1FICRd8yubQxh8zLOENZ9eFuPpS1elAHrJEZGlHVEE0uBj-1B1l6tkHM_GLubAQAmJzojDRzSXRRF2RqbYcN0F5paeHkrAr0KhE3YDu44ZGu1boY-nz9P67J235Bpcc_qbte1f3DiWz4fc3ZHHtNz35FW_MRtapkmHlqbr9uQ&k=6LfW6wATAAAAAHLqO2pb8bDBahxlMxNdo9g947u9"

payload={}
headers = {
  'authority': 'www.google.com',
  'cache-control': 'max-age=0',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'sec-ch-ua-full-version': '"96.0.4664.45"',
  'sec-ch-ua-arch': '"x86"',
  'sec-ch-ua-platform-version': '"10.0.0"',
  'sec-ch-ua-model': '""',
  'x-client-data': 'CJe2yQEIorbJAQjEtskBCKmdygEInpfLAQjq8ssBCNf8ywEI54TMAQi1hcwBCMuJzAEI0IvMAQibjswBCKyOzAEI3I7MAQjTj8wBCNqQzAEYjJ7LAQ==',
  'sec-fetch-site': 'none',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-user': '?1',
  'sec-fetch-dest': 'document'
}

response = requests.request("GET", url, headers=headers, data=payload)

with open(r"C:\Users\10449\Desktop\code\python\python_request\1.jpg","wb+") as f:
    f.write(response.content)