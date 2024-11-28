# *One Hotel*

---
*Hotel One* is a site based on a ficticous hotel, where users can create an account, search and book a hotel room, and manage their existing booking information.
This site is created with Django and runs PostgreSQL to manage a database of hotel room data and user booking data.

<!-- The live site can be found here: [Hotel One](LINK)!!!! -->

<!-- ![Responsive](documentation/images/amiresponsive.png) -->

## Deployment to GitHub Pages

This project was deployed with Heroku.

Steps to deploy on Heroku:

1. Create Heroku account
2. Via settings tab ensure Config Vars is set as:
    DISABLE_COLLECTSTATIC = 1
3.

## Features

- Users are greeted with a welcome page that provides a quic link to the search rooms page.
- The home page also provides links to all site pages and displays the current logged in user status.

### User Login

- New users are able to create an account username and password via the 'Register' tab.
- Users have the option to manage login or logout via links in the page header, the current logged in user status is displayed in the top right of the header.

### Room Search

- Found on the room search tab, users can filter all rooms by room features such as room type, bed type, view type.
These filters can be combined to find the exact room a user desires.

### Room Detail

- Once a desired room is found, users may click this link to read more detail about the room.
- If a user is logged in, they are able to select dates to create a reservation.
- Users have a link to directly view their existing bookings.

## User Stories

- As a traveler I want to request a hotel room booking.
- As a traveler I want the ability to view existing bookings and request edits.

- As a hotel employee I want to approve room bookings.
- As a hotel employee I want full control to edit existing bookings.

### First Time Visitor Goals

- First time visitors are met with a clear and simple way to search available hotel rooms.
Once the desired room is found it is possible to make a request a booking.

### Returning Visitor Goals

- Returning visitors have access to view existing bookngs status and request edits.

---

## Technologies Used

- [Django](https://www.djangoproject.com/) - framwork used to create Hotel One.
- [PostgreSQL](https://www.postgresql.org/) - relational database used to manage Hotel One backend.
- [Bootstrap](https://getbootstrap.com/) - used to manage the css of this project.
- [Heroku](https://www.heroku.com/home) - was used to deploy the project.
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) was used as the foundation of the site.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/css) - was used to add the styles and layout of the site.
- [Python](https://www.python.org/) - was used to create the site functions.
- [VSCode](https://code.visualstudio.com/) was used as the code editor.
- [GitHub](https://github.com/) was used to host the code of the website.
- [SourceTree](https://www.sourcetreeapp.com/) was used to manage the version control.
- [GIMP](https://www.gimp.org/) was used to edit and resize images.
- [OpenArt](https://openart.ai/home) was used to develop the hotel images used.
- [unsplash](unsplash.com) - provided free use images of the hotel rooms.
- Google Dev Tools was used for website testing.
- Google Light House was used for website testing.
<!-- - [Responsive Design Checker](https://responsivedesignchecker.com/) was used to check the responsiveness of the site on multiple screen sizes. -->
<!-- - [Am I responsive](https://ui.dev/amiresponsive) was used to generate an image of the site on different screen sizes. -->
<!-- - [Markup Validation Service](https://validator.w3.org/) Was used to validate the HTML code. -->
<!-- - [CSS Validation Service](https://jigsaw.w3.org/css-validator/) Was used to validate the CSS code. -->
<!-- - [JS Hint](https://jshint.com/) was used to validate the JavaScript code. -->

---

## Design

- Design of Hotel One is based on the Bootstrap template for ease of usage and clear design language.

## Testing

### Tests

<!-- - Screen size responsiveness of the website [Responsive Design Checker](https://responsivedesignchecker.com/) was used to view the site on multiple screen sizes.
  - The site responded as expected on all screen sizes, the game board is able to adjust to the screen size on page load.
- All buttons and links were tested on multiple devices.
  - All buttons are working as expected and linked to the correct locations.
- All clickable links have been checked for a change in mouse pointer.
  - All buttons change the mouse pointer as expected on all links
- All pages have been checked in multiple browser types including Chrome, Firefox, Edge
  - Moon Jumper is running without issues in all browsers tested -->

### Light House Tests

<!-- - See below for Chrome Light House test results on each web page. -->

#### Index page

<!-- ![Light House Index](documentation/images/lighthouse_index.png) -->

#### Game board page

<!-- ![Light House Game board](documentation/images/lighthouse_gameboard.png) -->

### Code Validation Tests

- See below the results of the JS, HTML and CSS validators.

#### HTML Validation Index

![HTML Validation Index](documentation/images/validatorhtml_index.png)

#### HTML Validation Game Board

![HTML Validation Game board](documentation/images/validatorhtml_gameboard.png)

#### CSS Validation

<!-- ![CSS Validation](documentation/images/validatorhtml_css.png) -->

#### JS Hints Index - No warnings or errors found

![JS Hints Index](documentation/images/jshint_index.png)

#### JS Hints Moon Jumper - No warnings or errors found

![JS Hints Moon Jumper](documentation/images/jshint_moonjumper.png)

### Resolved Bugs / Known Issues

<!-- - While adding multiple jump objects, the issue arose that no objects would get displayed. This is because at game load the jump objects array is empty and the first check is to see what object is loaded.
The solution was to create a "first jump object", on game start a "small rock" jump object is loaded to the first line of the jump array. Once the first object is loaded the random objects can be created to the jump object array.

- The jump object array would not get cleared after objects passed the game board. This was due to the first line in the array having a different format and no screen position to measure. The solution was to remove the first array line by checking the second array line. when the second object passed a screen position limit the first object is removed from the array. -->

### Open Bugs / Issues

- No open software bugs or issues are found.

### Future improvements

- Currently users must wait for admin booking approval, this could become an automated feature based on room availability.
- Automatic emails could be sent to users regarding booking status or other informaiton.
- User experience could be improved regarding managing existing bookings.

---

## Credits

### Media

- [OpenArt](https://openart.ai/home) was used to develop the main 'grand hotel' image on the welcome page.
- [unsplash](unsplash.com) - provided free use images of the hotel rooms.

### Acknowledgments

- [Iuliia Konovalova](https://github.com/IuliiaKonovalova) Who has been a knowledgeable and encouraging mentor on this project.
<!-- - [Kevin Powell](https://www.youtube.com/@KevinPowell) Who provided lessons on using CSS modals.
- [ImKennyYip](https://github.com/ImKennyYip/flappy-bird?tab=readme-ov-file) This project has been based on the lessons learned from ImKennyYip's YouTube tutorial on how to make Flappy Bird.
- [GitHub](https://pages.github.com/) Pages for free hosting of the live site.
- [w3school](https://www.w3schools.com) Was used as a reference for all html, css, and javascript questions.
- [Text compare](https://www.textcompare.org/) used to compare Moon Jumper to the reference Flappy Bird project. -->

### Code Refrences

- [stackoverflow](https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits) - this code was refreenced to create the booking code function "create_booking_code".
- [Matt Freire](https://youtu.be/vU0VeFN-abU?si=Hjk-YYMc2y1SorgN) - Matt Freire Youtube video assisted with how to create the rooms filter functions found in "FilterList"

## Additional Resources

- [Django for Beginners 5th Edition](https://www.amazon.de/Django-Beginners-5th-Modern-Applications/dp/173546726X) - A resorce for general Django topics.
- [Django 5 by Example](https://www.packtpub.com/en-us/product/django-5-by-example-9781805122340) - Additional examples on how to create Django apps.
