# Imports
import re
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options

# Setup driver and navigate to base url, run headless and mute any audio from opened session
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--mute-audio")
driver = webdriver.Chrome(options = chrome_options)
wait = WebDriverWait(driver, 20)
driver.get("https://www.youtube.com")
driver.maximize_window()

# On youtube homepage, search for a channel
search_box = driver.find_element_by_id("search")
search_icon_magnifier = driver.find_element_by_id("search-icon-legacy")

search_box.send_keys("theneedledrop")
search_icon_magnifier.click()

# Wait until the channel page has shown and click the target channel
channel_name = "h3[id = 'channel-title'] > span"
channel_name = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, channel_name)))
channel_name.click()

# Click on the videos tab of the target channel
videos = "div[ class = 'tab-content style-scope paper-tab']"
videos = wait.until(ec.visibility_of_any_elements_located((By.CSS_SELECTOR, videos)))
videos[1].click()

# Select the latest uploaded video
latest_video = 'div[id = "items"] > ytd-grid-video-renderer:not([class *= "horizontal"])'
latest_video = wait.until(ec.visibility_of_any_elements_located((By.CSS_SELECTOR,latest_video)))
latest_video[0].click()

# Check if the url contains the previous file ID, else read/parse the description
if driver.current_url in "lastidinfile":
    print('ID of previous video matches the previously held value, no new videos to parse')
else:
    # Fetch the video title and format for output
    video_title = 'h1[class *="title"]:not([hidden]) > yt-formatted-string'
    video_title = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, video_title)))
    video_title = video_title.get_attribute("innerText").replace("ALBUM REVIEW","").strip()
    
    # Click the more information button to expand the description
    more_info_button = 'ytd-expander[class="style-scope ytd-video-secondary-info-renderer"] > paper-button[id = "more"]'
    more_info_button = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, more_info_button)))
    more_info_button.click()

    # Fetch the entire video description
    video_description = 'div[id = "description"]'
    video_description = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, video_description)))
    video_description = video_description.get_attribute("innerText")

    # Extract the most and least favourite tracks part with string parsing
    fav_tracks = video_description.split("FAV TRACKS:")[1].split("LEAST FAV TRACK")[0].strip()
    least_fav_tracks = video_description.split("LEAST FAV TRACK")[1].split("\n")[0]

    # Use regular expressions to find the portion of the description of the form 'X/Y'
    album_score = re.search("[0-9]\/[0-9]+",video_description).group(0)

    # Print results for debugging
    print("Extracted album title: " + video_title)
    print("Extracted favourite tracks: " + fav_tracks)
    print("Extracted least favourite tracks: " + least_fav_tracks)
    print("Extracted Album Score: " + album_score)

# write to file 

# dispose of resources
driver.close()
driver.quit()
