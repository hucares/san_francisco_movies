Project: SF Movies
Track: Full-stack

Abstract
========
The SF Movies visualizer allows a user to search and visualize filming
locations on a map. A critical requirement is that the search should be
done. A JavaScript client communicates with a Flask backend.

Frontend
========
The front-end is written in D3.js and backbone.js. It fetches a JSON
with all the relevant location data and visualized it on Google Maps.

I selected frameworks and tools that would allow speedy and concise development.
The center-piece of the frontend was D3.js since it allowed it can create 
stunning visualizations very quickly. It is supremely concise and its
data-driven architechture minimizes the problem of state handling. I use a 
jQuery plugin to manage the autocomplete feature. I selected Google maps
on the basis of its good visual design, outstanding geocoding, and
StreetView integration.

I am profecient with JavaScript. I have extensive experience with
backbone.js and some experience with D3.js.

Backend
=======
The backend of the of the application is written in Flask with a
SQL backend. Local development employs sqllite while production uses the
Heroku provided postgres. There is a test suite included.

The backend was motivated by the requirement
of my chosen track rather than strict technical neccessity. The end
client can simply request a full JSON file of all movie locations and D3.js
is powerful enough to simply organize and visualize completely on the
client-side. Flask provides a minimalist framework to write RESTful
interfaces.

In lieu of of the application requirements, I imagined a hypothetical
customer that would consume a JSON REST interface. This API could
hypothetically be employed by the front-end though I chose not to
integrate it for the sake of simplicity and speed. Were the data to grow
to a point where D3.js became sluggish, I would then switch to consuming
the more atomic backend operations.

I have not used Flask ever and I have limited experience with Heroku.

API
===
GET /dump
returns entire database contents

GET /movie/[name]

GET /movie/[name]/locations

Extras
======
Resume: https://db.tt/K2M6VSGl
Github: https://github.com/vendettanine

Check out the Project Euler repo on my personal repo. I finished about
44 problems before a breach forced them to delete their accounts =(
https://github.com/vendettanine/project-euler

