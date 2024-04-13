# Introduction
The Logic Legends team presents a new usecase with the help of uAgents designed to solve the problem of wastage of water in farms due to inadeduate information available by the farmers. Usually a farm requires a certain amount of water on a regular basis that is predictable by certain factors such as crop type, farm size and gowth stage. The primary aim of this project is to assign the task of information gathering from different sources, deciding the water to be irrigated and controling the water irrigation system all by different agents.

# Features
<ol>
  <li>Farm Input: This data includes the location of the Farm, crop type, farm size, soil type, stage of crop growth.</li>
  <li>Weather Data Fetch: Using the location data provided, Weather Agent will seek the data from the 7timer API response such as temperature, humidity and rainfall.</li>
  <li>Irrigation Measurements: The amount of water reuired by the plant is fixed but this can be fulfilled by two way: 1. Irrigation 2. Rainfall. The amount of water saved due to rainfall will be predicted in advance.</li>
  <li>Pump Control: An important feature is that the Pump_Agent will get directions to irrigate such a time intervals and timer period for each irrigation step.</li>
</ol>
