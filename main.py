import undetected_chromedriver as uc
from dotenv import dotenv_values
import random
from Drivers.TinderDriver import TinderDriver

config = dotenv_values(".env")

def main():
    options = uc.ChromeOptions()
    options.user_data_dir = config["CHROME_PROFILE"] # type: ignore
    options.add_argument("--disable-notifications")

    driver = uc.Chrome(options=options)
    tinder = TinderDriver(driver)
    tinder.check_for_login()

    bytes = tinder.get_image()

    for i in range(100):
        tinder.handle_popup()
        r = random.random()
        if r < 0.7:
            tinder.dislike()
        else:
            tinder.like()

    while True:
        pass

if __name__ == '__main__':
    main()

# <div aria-label="Mo" role="img" class="Bdrs(8px) Bgz(cv) Bgp(c) StretchedBox" style="background-image: url(&quot;https://images-ssl.gotinder.com/u/goepUMwvAP1GnBb9EkumGT/3uXhF14KTTRpVxZ7VxfLC9.webp?Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6IiovdS9nb2VwVU13dkFQMUduQmI5RWt1bUdULyoiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE2NjgwNDU1NTl9fX1dfQ__&amp;Signature=BGjyQECEVcjrikahRQI2JojCNtdmy2NRGg-zqXmlDo5~CfpPuO0kiFDkHIHBpXrNZWL4DwBcpRj9VfeeXaPFW2-zQBXTX-AF8LqamFJBmz4Cz8cf6qGQ-48niy8U6voFL9MeB7bIUYhaaZxutboMEGUKuql6jZOO601T~snNby6Ra5~4kqJcWvuY3qt4qNgmRZSKluJdhiRCIUOIpLlO92-w2FIRf0jJCDb7bWQoGmWPBENK9q5eDdrGF2pZxVI8FOb4UmuuPv1HKkAnx2NNOFzlW9cll0RwXZGv2wXoEbwlnldSQbf3Qlc63M1IaZ1T7KoEyLTrk~J4q6Qcf~LLDw__&amp;Key-Pair-Id=K368TLDEUPA6OI&quot;); background-position: 50% 16.8724%; background-size: auto 143.627%;"></div>

# <div aria-label="Stacy" role="img" class="Bdrs(8px) Bgz(cv) Bgp(c) StretchedBox" style="background-image: url(&quot;https://images-ssl.gotinder.com/u/w5m9FxLripc4YkkojJpGjw/58Te29xPvBNPriM8DEwKNY.webp?Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6IiovdS93NW05RnhMcmlwYzRZa2tvakpwR2p3LyoiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE2NjgxMTk4ODF9fX1dfQ__&amp;Signature=OLHompniJIE3xnhA63Xvs3JdcbADGvo7AGtCpUwkAc-OcMmLrDTdQM6ej2AoTcRLHItICU-EivOgsslwfWlagNkBolBh1asEFnSFuoT-cKPfC4EHB5Vhbhxc~YHX7jRBVONw~tRJgj3BJlBby5f7VeCNfH1UnGpnVD5MVWq6mNjMe0nSKG2IoLQDeGR1xH-ub3HyUSOGa~0p6aY8FCdTFJzhUUVgj~OKG6RUFTccimdlezFPdWd8ur7LEE5fTMlUSR9JKks3uHQrB0PzmCe8CAtt09710jgqcpAOLsor9KqTGWmDrtukfa5kZXAt9uwEJ9s7hr2kBcGmAMNclZwVMQ__&amp;Key-Pair-Id=K368TLDEUPA6OI&quot;); background-position: 50% 16.8724%; background-size: auto 143.627%;"></div>