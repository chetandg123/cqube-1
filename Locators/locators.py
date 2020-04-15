class Locators():
    # Login page objects
    username = "exampleInputEmail"
    password = "exampleInputPassword"
    login = "/html/body/app-root/app-login/div/div[2]/div[2]/form/button"
    # home Page objects
    points = "leaflet-interactive"

    blocks = "/html/body/app-root/app-map-view/div/div[2]/div[1]/button[1]"
    cluster = "/html/body/app-root/app-map-view/div/div[2]/div[1]/button[2]"
    schools = "/html/body/app-root/app-map-view/div/div[2]/div[1]/button[3]"

    homebutton = "districtWise"

    select_district = "/html/body/app-root/app-map-view/div/div[2]/div[2]/select[1]"
    select_blocks = "/html/body/app-root/app-map-view/div/div[2]/div[2]/select[2]"
    select_clusters = "/html/body/app-root/app-map-view/div/div[2]/div[2]/select[3]"

    logout = "/html/body/app-root/app-map-view/div/div[1]/div[2]/div/div[2]/button[1]"
