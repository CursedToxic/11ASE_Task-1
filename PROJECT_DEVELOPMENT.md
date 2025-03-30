# 11ASE Task 1 2025 - WWeather App

#### By Victor Guo

## Requirements Definition
### Functional Requirements
**Data Retrieval:**\
 What does the user need to be able to view in the system?\
 The user needs to be able to choose what data to delete, however, this data must not be from the API itself. This ensures that the application does not break due to the user unknowingly deleting something within the API that might stop the program from functioning properly.

**User Interface:**\
 What is required for the user to interact with the system?\
 The ability to click on buttons and read text is needed to use the program. It should be extremely easy to navigate through the user interface and if the user cannot understand, there should be a navigation guide on top of the search bar.

**Data Display:**\
 The User must be able to read the data from the API but not be able to change without permission. This again helps keep the application running. The data must also be as accurate as possible in order to make sure that the user recieves the right information upon using the app.

### Non-Functional Requirements
**Performance:**\
 This program needs to run smoothly on even the oldest devices (the test will be my MacBook Air from 2013, an 11 year old machine which struggles to run the web browser). Performance should be maintained when using different platforms, so the user can user is confident that they can run it on their computer.

**Reliability:**\
 The system actually does need to be extremely reliable as the user's data is a top priority and must not be leaked, so the system needs to be extremely reliable and store the data securely on all operating systems, and must not be flagged as insecure on any of them. This way the user who is going to install the application can be sure that they are not harming their computer.

**Usability and Accessibility:**\
  The system needs to be easy to navigate so that people who are not very familiar with computers can easily understand how it works. All there will need to be is a how to file showing what each button leads to. This program will also need to work on all desktop operating systems (will test using Windows, MacOS and Some Linux Kernels), which will make it widely accessible and run with no compatibility issues.

## Determining Specifications
### Functional Specifications
**User Requirements:**\
What does the user need to be able to do? List all specifications here.\
The user needs to be able to easily navigate the application even if they have never encountered it before, hopefully even without the guide. 

**Inputs & Outputs:**\
What inputs will the system need to accept and what outputs will it need to display?\
inputs: text containing the city
outputs: weather for that city, this includes the temperature in degrees celsius and the weather description e.g. partly cloudy.
inputs: buttons
outputs: fetch and output data from the API.

**Core Features:**\
The program needs to accept user input so that they can enter the name of a valid city. Another aspect of function is the ability to detect invalid places so that the weather data that is displayed is as accurate as possible so that the user experience will not be negatively affected.The user needs to also be able to search for the place with a button once they have entered the name of the desired place into the search box (this would be preffered if the user could also press ENTER for the same function).

**User Interaction:**\
How will users interact with the system (e.g. command-line, GUI?) and what information will it need to provide to help users navigate?\
The program needs to be able to display the temperature and the description of the weather from the API in a GUI (Graphical User Interface). This makes it easy for the user to find exactly what they want without needing to know much about using a computer.

**Error Handling:**\
What possible errors could you face that need to be handled by the system?\
An error that could be faced that needs to be handled by the system is in the instance that the user enters an invalid location. This will be handled by a pop-up message that reads 'City Not Found'. 

### Non-Functional Specifications
**Performance:**\
The system should fetch weather data as fast as possible so that the user does not feel as though they are working with a bloated application. The application should also feel smooth while running, having smooth animations and seamless theme changes, ensuring that it performs well.

**Useability / Accessibility:**\
How might you make your application more accessible? What could you do with the User Interface to improve usability?\
The user interface must be at least semi-aesthetic in order to make the user feel at home, preventing strain due to unnecessary text. On top of this, the application should launch the first time after installing the dependencies so that the user needs minimal time to retrieve weather data.

**Reliability:**\
A potential issue that needs to be adressed is the incorrect data when fetching data from the API. An example of this is when the user searches up a city such as 'Zhuzhou' (real place) and it comes up as 'Jianning' instead. This cannot be fixed as there seems to be a mismatch of data from the API itself (it labels Zhuzhou as Jianning and Jianning as something else.) Another issue is that the current weather app cannot distinguish places with the same name. These can hopefully be fixed easily.

## Design
### Gantt Chart
![alt text](images/Gantt%20Chart.png)
Link to Gantt Chart: https://lucid.app/lucidspark/162a4a9b-0462-4f05-9b21-b1997af60854/edit?invitationId=inv_9c51b1d8-6a9c-4b3f-bf6d-b49fa2d28f11&page=uDe-dIt-NWfS#

### Structure Chart

### Data Dictionaries

## Development

## Integration

## Testing and Debugging

## Installation

## Maintenance