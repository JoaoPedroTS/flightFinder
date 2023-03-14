# flightFinder
This aplication is developed to identify good flight deals. This is done by using a API called [sheety](https://sheety.co/) to keep track of prices cut off for
diferent destinations in a google sheet. In this sheet the API always read the current cut off price and update when a better one is discovered

<p align="center">
  <img src="https://user-images.githubusercontent.com/54846443/225067617-296fda6c-1a82-417e-b5a4-6ea6dc0bcf46.png" />
</p>

The prices and the destinations are setted manually, and the program will just look for flight destinations that are on the sheet.
The flight search is done by another API called [tequila](https://partners.kiwi.com/). The search is based on a series of criteria, such as origin, date from, 
max stop overs and others. All this parameters are hard coded in the project, just for simplicity. But could be adapeted to work with inputed values.
Every time the program runs it prints a output with a search result for each destination

<p align="center">
  <img src="https://user-images.githubusercontent.com/54846443/225073237-b9770ab9-eff4-41fc-a043-5bc87f4ecf01.png" />
</p>

This app also uses a API called [twilio](https://www.twilio.com) to send SMS whenever a good deal is found

<p align="center">
  <img src="https://user-images.githubusercontent.com/54846443/225076782-ad905085-2831-45d0-b3ee-6a6771d9a226.png" />
</p>
