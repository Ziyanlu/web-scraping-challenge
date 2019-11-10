{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup\n",
    "import requests\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# NASA Mars News"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "url = 'https://mars.nasa.gov/news/'\n",
    "browser.visit(url)\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'lxml')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "results = soup.find_all('div', class_='list_text')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NASA's Mars 2020 Heads Into the Test Chamber\n",
      "In this time-lapse video taken at JPL, engineers move the Mars 2020 rover into a large vacuum chamber for testing in Mars-like environmental conditions.\n",
      "------------------------------------------------------------------\n",
      "Screening Soon: 'The Pathfinders' Trains Lens on Mars\n",
      "With the Mars 2020 mission ramping up, the documentary — the first of four about past JPL missions to the Red Planet to be shown at Caltech — tells a gripping backstory.\n",
      "------------------------------------------------------------------\n",
      "InSight's 'Mole' Team Peers into the Pit\n",
      "Efforts to save the heat probe continue.\n",
      "------------------------------------------------------------------\n",
      "Common Questions about InSight's 'Mole'\n",
      "There's a new plan to get InSight's \"mole\" moving again. The following Q&As with two members of the team answer some of the most common questions about the burrowing device, part of a science instrument called the Heat Flow and Physical Properties Package (HP3).\n",
      "------------------------------------------------------------------\n",
      "Mars 2020 Stands on Its Own Six Wheels\n",
      "In time-lapse video, taken at JPL, captures the first time NASA's Mars 2020 rover carries its full weight on its legs and wheels.\n",
      "------------------------------------------------------------------\n",
      "New Selfie Shows Curiosity, the Mars Chemist\n",
      "The NASA rover performed a special chemistry experiment at the location captured in its newest self-portrait.\n",
      "------------------------------------------------------------------\n",
      "Naming a NASA Mars Rover Can Change Your Life\n",
      "Want to name the robotic scientist NASA is sending to Mars in 2020? The student who named Curiosity — the rover currently exploring Mars — will tell you this is an opportunity worth taking.\n",
      "------------------------------------------------------------------\n",
      "Mars 2020 Unwrapped and Ready for More Testing\n",
      "In time-lapse video, bunny-suited engineers remove the inner layer of protective foil on NASA's Mars 2020 rover after it was relocated for testing.\n",
      "------------------------------------------------------------------\n",
      "HiRISE Views NASA's InSight and Curiosity on Mars\n",
      "New images taken from space offer the clearest orbital glimpse yet of InSight as well as a view of Curiosity rolling along.\n",
      "------------------------------------------------------------------\n",
      "NASA's Curiosity Rover Finds an Ancient Oasis on Mars\n",
      "New evidence suggests salty, shallow ponds once dotted a Martian crater — a sign of the planet's drying climate.\n",
      "------------------------------------------------------------------\n",
      "NASA's Mars 2020 Rover Tests Descent-Stage Separation\n",
      "A crane lifts the rocket-powered descent stage away from NASA's Mars 2020 rover after technicians tested the pyrotechnic charges that separate the two spacecraft.\n",
      "------------------------------------------------------------------\n",
      "NASA's Push to Save the Mars InSight Lander's Heat Probe\n",
      "The scoop on the end of the spacecraft's robotic arm will be used to 'pin' the mole against the wall of its hole.\n",
      "------------------------------------------------------------------\n",
      "NASA's InSight 'Hears' Peculiar Sounds on Mars\n",
      "Listen to the marsquakes and other, less-expected sounds that the Mars lander has been detecting.\n",
      "------------------------------------------------------------------\n",
      "NASA Mars Mission Connects With Bosnian and Herzegovinian Town\n",
      "A letter from NASA was presented to the mayor of Jezero, Bosnia-Herzegovina, honoring the connection between the town and Jezero Crater, the Mars 2020 rover landing site.\n",
      "------------------------------------------------------------------\n",
      "Deadline Closing for Names to Fly on NASA's Next Mars Rover\n",
      "You have until Sept. 30 to send your names to Mars aboard the Mars 2020 rover. \n",
      "------------------------------------------------------------------\n",
      "NASA Wins Two Emmy Awards for Interactive Mission Coverage\n",
      "NASA-JPL's coverage of the Mars InSight landing earns one of the two wins, making this the NASA center's second Emmy.\n",
      "------------------------------------------------------------------\n",
      "NASA's Mars 2020 Comes Full Circle\n",
      "Aiming to pinpoint the Martian vehicle's center of gravity, engineers took NASA's 2,300-pound Mars 2020 rover for a spin in the clean room at JPL. \n",
      "------------------------------------------------------------------\n",
      "NASA Invites Students to Name Mars 2020 Rover\n",
      "Through Nov. 1, K-12 students in the U.S. are encouraged to enter an essay contest to name NASA's next Mars rover.\n",
      "------------------------------------------------------------------\n",
      "NASA's Mars Helicopter Attached to Mars 2020 Rover \n",
      "The helicopter will be first aircraft to perform flight tests on another planet.\n",
      "------------------------------------------------------------------\n",
      "What's Mars Solar Conjunction, and Why Does It Matter?\n",
      "NASA spacecraft at Mars are going to be on their own for a few weeks when the Sun comes between Mars and Earth, interrupting communications.\n",
      "------------------------------------------------------------------\n",
      "Scientists Explore Outback as Testbed for Mars \n",
      "Australia provides a great place for NASA's Mars 2020 and the ESA-Roscosmos ExoMars scientists to hone techniques in preparation for searching for signs ancient life on Mars.\n",
      "------------------------------------------------------------------\n",
      "NASA-JPL Names 'Rolling Stones Rock' on Mars\n",
      "NASA's Mars InSight mission honored one of the biggest bands of all time at Pasadena concert.\n",
      "------------------------------------------------------------------\n",
      "Robotic Toolkit Added to NASA's Mars 2020 Rover\n",
      "The bit carousel, which lies at the heart of the rover's Sample Caching System, is now aboard NASA's newest rover. \n",
      "------------------------------------------------------------------\n",
      "Space Samples Link NASA's Apollo 11 and Mars 2020\n",
      "While separated by half a century, NASA's Apollo 11 and Mars 2020 missions share the same historic goal: returning samples to Earth.\n",
      "------------------------------------------------------------------\n",
      "Small Satellite Mission of the Year\n",
      "The first interplanetary CubeSats were recognized by the engineering community with the 2019 Small Satellite Mission of the Year award.\n",
      "------------------------------------------------------------------\n",
      "NASA 'Optometrists' Verify Mars 2020 Rover's 20/20 Vision\n",
      "Mars 2020 rover underwent an eye exam after several cameras were installed on the rover.\n",
      "------------------------------------------------------------------\n",
      "New Finds for Mars Rover, Seven Years After Landing\n",
      "NASA's Curiosity rover is discovering odd rocks halfway into a region called the \"clay-bearing unit.\"\n",
      "------------------------------------------------------------------\n",
      "MEDLI2 Installation on Mars 2020 Aeroshell Begins\n",
      "Hardware installed onto NASA's Mars 2020 entry vehicle this week will help to increase the safety of future Mars landings.\n",
      "------------------------------------------------------------------\n",
      "NASA's Mars 2020 Rover Does Biceps Curls \n",
      "In this time-lapse video, the robotic arm on NASA's Mars 2020 rover maneuvers its 88-pound (40-kilogram) sensor-laden turret as it moves from a deployed to stowed configuration.\n",
      "------------------------------------------------------------------\n",
      "Fueling of NASA's Mars 2020 Rover Power System Begins\n",
      "NASA gives the go-ahead to fuel the Mars 2020 rover's Multi-Mission Radioisotope Thermoelectric Generator, which will power rover and help keep it warm while exploring Mars.\n",
      "------------------------------------------------------------------\n",
      "What Does a Marsquake Look Like?\n",
      "InSight scientists used a special \"shake room\" to demonstrate the differences between quakes on Earth, the Moon and Mars.\n",
      "------------------------------------------------------------------\n",
      "Mars 2020 Rover: T-Minus One Year and Counting \n",
      "The launch period for NASA's next rover, Mars 2020, opens exactly one year from today, July 17, 2020, and extends through Aug. 5, 2020.\n",
      "------------------------------------------------------------------\n",
      "NASA Racks Up Two Emmy Nominations for Mission Coverage\n",
      "JPL's coverage of the Mars InSight mission is among the efforts that will be up for an award in mid-September.\n",
      "------------------------------------------------------------------\n",
      "Want to Colonize Mars? Aerogel Could Help\n",
      "Researchers are studying whether a wonder material used in Mars rovers could help warm parts of the Red Planet rich in water ice.\n",
      "------------------------------------------------------------------\n",
      "A Rover Pit Stop at JPL\n",
      "Working like a finely honed machine, a team of engineers in this time-lapse video clip install test wheels on another finely honed machine: NASA's Mars 2020 rover.\n",
      "------------------------------------------------------------------\n",
      "Mars 2020 Rover Gets a Super Instrument\n",
      "With its rock-zapping laser, the SuperCam will enable the science team to identify the chemical and mineral makeup of its targets on the Red Planet.\n",
      "------------------------------------------------------------------\n",
      "A Neil Armstrong for Mars: Landing the Mars 2020 Rover\n",
      "NASA's newest rover will have an autopilot called Terrain-Relative Navigation.\n",
      "------------------------------------------------------------------\n",
      "NASA's InSight Uncovers the 'Mole' \n",
      "The lander's robotic arm has successfully removed a piece of hardware blocking the view of its digging device in order to help with recovery efforts.\n",
      "------------------------------------------------------------------\n",
      "Mars 2020 Rover's 7-Foot-Long Robotic Arm Installed\n",
      "The main robotic arm has been installed on NASA's newest rover. When complete, the arm will enable the rover to hold and use science tools like a human geologist would.\n",
      "------------------------------------------------------------------\n",
      "NASA Selects Partners for Mars 2020 'Name the Rover' Contest, Seeks Judges\n",
      "The contest for U.S. schoolchildren will open in fall 2019, but judges can sign up now.\n",
      "------------------------------------------------------------------\n"
     ]
    }
   ],
   "source": [
    "titles = []\n",
    "paragraphs = []\n",
    "for result in results:\n",
    "    title = result.find('a').text\n",
    "    paragraph = result.find('div', class_='article_teaser_body').text\n",
    "    \n",
    "    titles.append(title)\n",
    "    paragraphs.append(paragraph)\n",
    "    print(title)\n",
    "    print(paragraph)\n",
    "    print('------------------------------------------------------------------')\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "most_recent_title = titles[0]\n",
    "most_recent_paragraph = paragraphs[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Most recent news from NASA Mars News\n",
      "News title: NASA's Mars 2020 Heads Into the Test Chamber\n",
      "News body: In this time-lapse video taken at JPL, engineers move the Mars 2020 rover into a large vacuum chamber for testing in Mars-like environmental conditions.\n"
     ]
    }
   ],
   "source": [
    "print('Most recent news from NASA Mars News')\n",
    "print(f\"News title: {most_recent_title}\")\n",
    "print(f\"News body: {most_recent_paragraph}\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# JPL Mars Space Images - Featured Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "browser.visit(img_url)\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'lxml')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "image_results = soup.find_all('div', class_ = \"carousel_items\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<article alt=\"A Storm of Change\" class=\"carousel_item\" style=\"background-image: url('/spaceimages/images/wallpaper/PIA23436-1920x1200.jpg');\">\n",
      "<div class=\"default floating_text_area ms-layer\">\n",
      "<h2 class=\"category_title\">\n",
      "</h2>\n",
      "<h2 class=\"brand_title\">\n",
      "\t\t\t\t  FEATURED IMAGE\n",
      "\t\t\t\t</h2>\n",
      "<h1 class=\"media_feature_title\">\n",
      "\t\t\t\t  A Storm of Change\t\t\t\t</h1>\n",
      "<div class=\"description\">\n",
      "</div>\n",
      "<footer>\n",
      "<a class=\"button fancybox\" data-description=\"NASAs Juno spacecraft shows Jupiters iconic Great Red Spot, a storm that has been raging since at least the 1800s.\" data-fancybox-group=\"images\" data-fancybox-href=\"/spaceimages/images/mediumsize/PIA23436_ip.jpg\" data-link=\"/spaceimages/details.php?id=PIA23436\" data-title=\"A Storm of Change\" id=\"full_image\">\n",
      "\t\t\t\t\tFULL IMAGE\n",
      "\t\t\t\t  </a>\n",
      "</footer>\n",
      "</div>\n",
      "<div class=\"gradient_container_top\"></div>\n",
      "<div class=\"gradient_container_bottom\"></div>\n",
      "</article>\n"
     ]
    }
   ],
   "source": [
    "for image_result in image_results:\n",
    "    image = image_result.find('article',class_='carousel_item')\n",
    "    print(image)\n",
    "featured_image = image['style'].split(\"'\")[1]\n",
    "featured_image_url = \"https://www.jpl.nasa.gov\"+ featured_image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA23436-1920x1200.jpg'"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "featured_image_url"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Mars Weather"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://twitter.com/marswxreport?lang=en'\n",
    "browser.visit(url)\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'lxml')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "posts = soup.find_all('div', class_='js-tweet-text-container')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['InSight sol 338 (2019-11-08) low -102.5ºC (-152.5ºF) high -24.0ºC (-11.1ºF)\\nwinds from the SSE at 5.3 m/s (11.9 mph) gusting to 19.6 m/s (43.9 mph)\\npressure at 6.90 hPapic.twitter.com/VxWNunPM5q',\n",
       " 'InSight sol 337 (2019-11-07) low -101.8ºC (-151.2ºF) high -24.0ºC (-11.3ºF)\\nwinds from the SSE at 4.9 m/s (11.0 mph) gusting to 21.2 m/s (47.5 mph)\\npressure at 6.90 hPa',\n",
       " 'InSight sol 336 (2019-11-06) low -101.4ºC (-150.6ºF) high -24.0ºC (-11.2ºF)\\nwinds from the SSE at 4.7 m/s (10.6 mph) gusting to 18.7 m/s (41.9 mph)\\npressure at 6.90 hPapic.twitter.com/RIAb2fzSY4',\n",
       " 'InSight sol 335 (2019-11-05) low -100.6ºC (-149.1ºF) high -24.3ºC (-11.8ºF)\\nwinds from the SSE at 4.9 m/s (10.9 mph) gusting to 19.9 m/s (44.5 mph)\\npressure at 6.90 hPa',\n",
       " 'InSight sol 334 (2019-11-04) low -100.0ºC (-148.1ºF) high -23.8ºC (-10.8ºF)\\nwinds from the SSW at 5.1 m/s (11.4 mph) gusting to 19.9 m/s (44.4 mph)\\npressure at 7.00 hPapic.twitter.com/D4EX1MROay',\n",
       " 'InSight sol 333 (2019-11-03) low -100.8ºC (-149.4ºF) high -25.8ºC (-14.4ºF)\\nwinds from the SSW at 4.9 m/s (11.0 mph) gusting to 18.0 m/s (40.4 mph)\\npressure at 6.90 hPa',\n",
       " 'InSight sol 332 (2019-11-02) low -99.8ºC (-147.7ºF) high -25.2ºC (-13.3ºF)\\nwinds from the SSW at 4.1 m/s (9.2 mph) gusting to 18.7 m/s (41.9 mph)\\npressure at 6.90 hPa',\n",
       " 'InSight sol 331 (2019-11-01) low -100.9ºC (-149.6ºF) high -24.6ºC (-12.3ºF)\\nwinds from the SSE at 5.2 m/s (11.6 mph) gusting to 18.5 m/s (41.4 mph)\\npressure at 7.00 hPapic.twitter.com/jicxvaUZh1',\n",
       " 'InSight sol 330 (2019-10-31) low -101.8ºC (-151.3ºF) high -24.8ºC (-12.6ºF)\\nwinds from the SSE at 5.4 m/s (12.2 mph) gusting to 20.8 m/s (46.5 mph)\\npressure at 7.00 hPapic.twitter.com/nMo54muCBo',\n",
       " 'InSight sol 329 (2019-10-30) low -101.5ºC (-150.7ºF) high -25.0ºC (-13.0ºF)\\nwinds from the SSE at 5.2 m/s (11.6 mph) gusting to 19.2 m/s (42.8 mph)\\npressure at 7.00 hPapic.twitter.com/LqWHBwF74A',\n",
       " 'InSight sol 328 (2019-10-29) low -102.3ºC (-152.2ºF) high -25.2ºC (-13.3ºF)\\nwinds from the SSE at 4.9 m/s (10.9 mph) gusting to 18.3 m/s (40.9 mph)\\npressure at 7.00 hPa',\n",
       " 'InSight sol 327 (2019-10-28) low -102.6ºC (-152.7ºF) high -25.3ºC (-13.5ºF)\\nwinds from the SSE at 5.6 m/s (12.5 mph) gusting to 19.6 m/s (43.8 mph)\\npressure at 7.00 hPapic.twitter.com/B3xpG54HEx',\n",
       " 'InSight sol 326 (2019-10-27) low -101.4ºC (-150.5ºF) high -23.7ºC (-10.7ºF)\\nwinds from the SSE at 5.2 m/s (11.5 mph) gusting to 18.2 m/s (40.8 mph)\\npressure at 7.00 hPapic.twitter.com/zSxE0oiy1D',\n",
       " 'You gotta keep ‘em separated \\n\\nEngineers and technicians working on the #Mars2020 spacecraft look on as a crane lifts the rocket-powered descent stage away from the rover after a test: https://go.nasa.gov/2IpH4I3\\xa0pic.twitter.com/tBLCWS0b5q',\n",
       " 'InSight sol 325 (2019-10-26) low -102.0ºC (-151.7ºF) high -24.0ºC (-11.2ºF)\\nwinds from the SSE at 4.9 m/s (11.0 mph) gusting to 19.1 m/s (42.7 mph)\\npressure at 7.00 hPapic.twitter.com/P20JfRjcVi',\n",
       " 'InSight sol 324 (2019-10-25) low -102.4ºC (-152.3ºF) high -24.8ºC (-12.6ºF)\\nwinds from the SSE at 5.4 m/s (12.0 mph) gusting to 18.1 m/s (40.5 mph)\\npressure at 7.00 hPapic.twitter.com/goHqhpyD8O',\n",
       " 'InSight sol 322 (2019-10-23) pressure at 7.00 hPa',\n",
       " 'InSight sol 321 (2019-10-22) low -102.9ºC (-153.2ºF) high -24.6ºC (-12.3ºF)\\nwinds from the SSE at 4.8 m/s (10.8 mph) gusting to 18.6 m/s (41.6 mph)\\npressure at 7.10 hPapic.twitter.com/FsE4d1Fskt',\n",
       " 'InSight sol 320 (2019-10-21) low -102.4ºC (-152.3ºF) high -25.6ºC (-14.0ºF)\\nwinds from the SSE at 4.7 m/s (10.5 mph) gusting to 18.5 m/s (41.4 mph)\\npressure at 7.10 hPapic.twitter.com/TxQmtXP7xo',\n",
       " 'InSight sol 319 (2019-10-19) low -101.5ºC (-150.7ºF) high -25.5ºC (-13.9ºF)\\nwinds from the SSE at 4.6 m/s (10.4 mph) gusting to 18.4 m/s (41.2 mph)\\npressure at 7.10 hPapic.twitter.com/gdBUdujdVM']"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "weather_of_Mars = []\n",
    "for post in posts:\n",
    "    weather = post.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text\n",
    "    weather_of_Mars.append(weather)\n",
    "weather_of_Mars\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "InSight sol 338 (2019-11-08) low -102.5ºC (-152.5ºF) high -24.0ºC (-11.1ºF)\n",
      "winds from the SSE at 5.3 m/s (11.9 mph) gusting to 19.6 m/s (43.9 mph)\n",
      "pressure at 6.90 hPapic.twitter.com/VxWNunPM5q\n"
     ]
    }
   ],
   "source": [
    "mars_weather = weather_of_Mars[0]\n",
    "print(mars_weather)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Mars Facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://space-facts.com/mars/'\n",
    "browser.visit(url)\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'lxml')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "tables = soup.find_all('table', class_='tablepress tablepress-id-p-mars')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[                      0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       " 3                Moons:            2 (Phobos & Deimos)\n",
       " 4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                   -87 to -5 °C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers,\n",
       "   Mars - Earth Comparison             Mars            Earth\n",
       " 0               Diameter:         6,779 km        12,742 km\n",
       " 1                   Mass:  6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       " 2                  Moons:                2                1\n",
       " 3      Distance from Sun:   227,943,824 km   149,598,262 km\n",
       " 4         Length of Year:   687 Earth days      365.24 days\n",
       " 5            Temperature:    -153 to 20 °C      -88 to 58°C,\n",
       "                       0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       " 3                Moons:            2 (Phobos & Deimos)\n",
       " 4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                   -87 to -5 °C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers]"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "url='https://space-facts.com/mars/'\n",
    "tables = pd.read_html(url)\n",
    "tables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Equatorial Diameter:</td>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Polar Diameter:</td>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Orbit Distance:</td>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Orbit Period:</td>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Surface Temperature:</td>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>First Record:</td>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Recorded By:</td>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                      0                              1\n",
       "0  Equatorial Diameter:                       6,792 km\n",
       "1       Polar Diameter:                       6,752 km\n",
       "2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       "3                Moons:            2 (Phobos & Deimos)\n",
       "4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       "5         Orbit Period:           687 days (1.9 years)\n",
       "6  Surface Temperature:                   -87 to -5 °C\n",
       "7         First Record:              2nd millennium BC\n",
       "8          Recorded By:           Egyptian astronomers"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df=tables[0]\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Equatorial Diameter:</td>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Polar Diameter:</td>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Orbit Distance:</td>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Orbit Period:</td>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Surface Temperature:</td>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>First Record:</td>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Recorded By:</td>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                      0                              1\n",
       "0  Equatorial Diameter:                       6,792 km\n",
       "1       Polar Diameter:                       6,752 km\n",
       "2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       "3                Moons:            2 (Phobos & Deimos)\n",
       "4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       "5         Orbit Period:           687 days (1.9 years)\n",
       "6  Surface Temperature:                   -87 to -5 °C\n",
       "7         First Record:              2nd millennium BC\n",
       "8          Recorded By:           Egyptian astronomers"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Mars_df = df.rename(columns={'0': 'Mars Facts',\n",
    "                          'Mars': 'Value'})\n",
    "Mars_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "html_table = Mars_df.to_html('table.html')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Mars Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "browser.visit(url)\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'lxml')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "results = soup.find_all('div', class_='description')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cerberus Hemisphere Enhanced\n",
      "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/search/map/Mars/Viking/cerberus_enhanced\n",
      "------------------------------------------------------------------\n",
      "Schiaparelli Hemisphere Enhanced\n",
      "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/search/map/Mars/Viking/schiaparelli_enhanced\n",
      "------------------------------------------------------------------\n",
      "Syrtis Major Hemisphere Enhanced\n",
      "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/search/map/Mars/Viking/syrtis_major_enhanced\n",
      "------------------------------------------------------------------\n",
      "Valles Marineris Hemisphere Enhanced\n",
      "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/search/map/Mars/Viking/valles_marineris_enhanced\n",
      "------------------------------------------------------------------\n"
     ]
    }
   ],
   "source": [
    "titles = []\n",
    "image_urls = []\n",
    "hemisphere_image_urls = []\n",
    "\n",
    "for result in results:\n",
    "    title = result.find('h3').text\n",
    "    \n",
    "    image = result.find('a', class_ ='itemLink product-item')['href']\n",
    "    image_url = url + image\n",
    "    \n",
    "    titles.append(title)\n",
    "    image_urls.append(image_url)\n",
    "    hemisphere_image_urls.append({'title':title,\n",
    "                                  'image_url':image_url})\n",
    "    print(title)\n",
    "    print(image_url)\n",
    "    print('------------------------------------------------------------------')\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere Enhanced',\n",
       "  'image_url': 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/search/map/Mars/Viking/cerberus_enhanced'},\n",
       " {'title': 'Schiaparelli Hemisphere Enhanced',\n",
       "  'image_url': 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/search/map/Mars/Viking/schiaparelli_enhanced'},\n",
       " {'title': 'Syrtis Major Hemisphere Enhanced',\n",
       "  'image_url': 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/search/map/Mars/Viking/syrtis_major_enhanced'},\n",
       " {'title': 'Valles Marineris Hemisphere Enhanced',\n",
       "  'image_url': 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/search/map/Mars/Viking/valles_marineris_enhanced'}]"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'news_title': \"NASA's Mars 2020 Heads Into the Test Chamber\", 'news_paragraph': 'In this time-lapse video taken at JPL, engineers move the Mars 2020 rover into a large vacuum chamber for testing in Mars-like environmental conditions.', 'featuredimage_url': 'https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA23436-1920x1200.jpg', 'marsweather': 'InSight sol 338 (2019-11-08) low -102.5ºC (-152.5ºF) high -24.0ºC (-11.1ºF)\\nwinds from the SSE at 5.3 m/s (11.9 mph) gusting to 19.6 m/s (43.9 mph)\\npressure at 6.90 hPapic.twitter.com/VxWNunPM5q', 'marsfacts': None, 'hemisphereimage_urls': [{'title': 'Cerberus Hemisphere Enhanced', 'image_url': 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/search/map/Mars/Viking/cerberus_enhanced'}, {'title': 'Schiaparelli Hemisphere Enhanced', 'image_url': 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/search/map/Mars/Viking/schiaparelli_enhanced'}, {'title': 'Syrtis Major Hemisphere Enhanced', 'image_url': 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/search/map/Mars/Viking/syrtis_major_enhanced'}, {'title': 'Valles Marineris Hemisphere Enhanced', 'image_url': 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/search/map/Mars/Viking/valles_marineris_enhanced'}]}\n"
     ]
    }
   ],
   "source": [
    "mars_info={\"news_title\":most_recent_title,\n",
    "           \"news_paragraph\":most_recent_paragraph,\n",
    "           \"featuredimage_url\":featured_image_url,\n",
    "           \"marsweather\":mars_weather,\n",
    "           \"marsfacts\":html_table,\n",
    "           \"hemisphereimage_urls\":hemisphere_image_urls  \n",
    "          }\n",
    "print(mars_info)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Store mars_info in MongoDB"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pymongo\n",
    "conn = 'mongodb://localhost:27017'\n",
    "client = pymongo.MongoClient(conn)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "db = client.MarsDB"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'_id': ObjectId('5dc63becf9a762e80b578afc'), 'news_title': \"NASA's Mars 2020 Heads Into the Test Chamber\", 'news_paragraph': 'In this time-lapse video taken at JPL, engineers move the Mars 2020 rover into a large vacuum chamber for testing in Mars-like environmental conditions.', 'featuredimage_url': 'https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA19046-1920x1200.jpg', 'marsweather': 'InSight sol 336 (2019-11-06) low -101.4ºC (-150.6ºF) high -24.0ºC (-11.2ºF)\\nwinds from the SSE at 4.7 m/s (10.6 mph) gusting to 18.7 m/s (41.9 mph)\\npressure at 6.90 hPapic.twitter.com/RIAb2fzSY4', 'marsfacts': None, 'hemisphereimage_urls': [{'title': 'Cerberus Hemisphere Enhanced', 'image_url': 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/search/map/Mars/Viking/cerberus_enhanced'}, {'title': 'Schiaparelli Hemisphere Enhanced', 'image_url': 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/search/map/Mars/Viking/schiaparelli_enhanced'}, {'title': 'Syrtis Major Hemisphere Enhanced', 'image_url': 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/search/map/Mars/Viking/syrtis_major_enhanced'}, {'title': 'Valles Marineris Hemisphere Enhanced', 'image_url': 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/search/map/Mars/Viking/valles_marineris_enhanced'}]}\n",
      "{'_id': ObjectId('5dc71bf1e25c798ec390ef64'), 'news_title': \"NASA's Mars 2020 Heads Into the Test Chamber\", 'news_paragraph': 'In this time-lapse video taken at JPL, engineers move the Mars 2020 rover into a large vacuum chamber for testing in Mars-like environmental conditions.', 'featuredimage_url': 'https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA23436-1920x1200.jpg', 'marsweather': 'InSight sol 338 (2019-11-08) low -102.5ºC (-152.5ºF) high -24.0ºC (-11.1ºF)\\nwinds from the SSE at 5.3 m/s (11.9 mph) gusting to 19.6 m/s (43.9 mph)\\npressure at 6.90 hPapic.twitter.com/VxWNunPM5q', 'marsfacts': None, 'hemisphereimage_urls': [{'title': 'Cerberus Hemisphere Enhanced', 'image_url': 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/search/map/Mars/Viking/cerberus_enhanced'}, {'title': 'Schiaparelli Hemisphere Enhanced', 'image_url': 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/search/map/Mars/Viking/schiaparelli_enhanced'}, {'title': 'Syrtis Major Hemisphere Enhanced', 'image_url': 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/search/map/Mars/Viking/syrtis_major_enhanced'}, {'title': 'Valles Marineris Hemisphere Enhanced', 'image_url': 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/search/map/Mars/Viking/valles_marineris_enhanced'}]}\n"
     ]
    }
   ],
   "source": [
    "mars = db.mars.find()\n",
    "for info in mars:\n",
    "    print(info)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<pymongo.results.InsertOneResult at 0x19d9b191a88>"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "db.mars.insert_one(\n",
    "          {\"news_title\":most_recent_title,\n",
    "           \"news_paragraph\":most_recent_paragraph,\n",
    "           \"featuredimage_url\":featured_image_url,\n",
    "           \"marsweather\":mars_weather,\n",
    "           \"marsfacts\":html_table,\n",
    "           \"hemisphereimage_urls\":hemisphere_image_urls\n",
    "          }\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
