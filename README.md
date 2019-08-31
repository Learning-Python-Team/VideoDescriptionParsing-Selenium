# Video Description Parsing With Selenium
Project to automate fetching details of album reviews that exist in a YouTube video description with a consistent format. Selenium Web Framework (primarily used for Automated Testing) is used as a quick and easy way to extract data without needing to utilise REST calls.

# Project Stages

### Phase 1: Automating Retrieval/Parsing of YouTube Description (Current)
Selenium Python is used to open a headless Chrome session, navigate to a channel that posts album reviews, and extracts the Album details, least and favourite tracks and outputs them to the console

## Potential Future Stages
### Phase 2: Content export to file/data store
Build upon current code to run script on a schedule, export results to a data store and add checking for if the fetched video has already been added to the data store.

### Phase 3/Extension Project: Usage of the YouTube REST API to fetch and Parse Data
Selenium has been used as a simple way to extract the neccessary information, but could be performed more elegantly using REST. An extension to this project would be to provide the same functionality (perhaps with variable channel names) using the YouTube API(if possible) to parse more video descriptions.

### Improvements:
- Object Orientation
- Auto update chromedriver to used Chrome Versionm
- Add Error Logging, improve parsing/recovery from failures

### Drawbacks:
- Manual Update of ChromeDriver exe are needed to align with current client Chrome Version
- Relies upon a consistent format for description
