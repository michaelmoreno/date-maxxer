import undetected_chromedriver as uc
from dotenv import dotenv_values
from Drivers.TinderDriver import TinderDriver

config = dotenv_values(".env")

def main():
    options = uc.ChromeOptions()
    options.user_data_dir = config["CHROME_PROFILE"] # type: ignore
    options.add_argument("--disable-notifications")

    driver = uc.Chrome(options=options)
    tinder = TinderDriver(driver, {'races': ['asian', 'latino hispanic'], 'genders': ['Woman']})
    tinder.check_for_login()

    tinder.run()
    

if __name__ == '__main__':
    main()
