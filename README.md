# Coding-challenge

# Instructions
  *Install Python3
  *Install Pandas Library
  *Install Json Library
  *Install OS Library
  
# DMV Appointment Scheduler

## Challenge

Create an appointment scheduler application for the Department of Motor Vehicles (DMV).

### Data Set

* Customer records
  * 5,000 total records
  * Available data:
    * Id
    * Service type
    * Appointment duration
* Teller records
  * 150 total records
  * Available data:
    * Id
    * Specialty type
    * Multiplier

### Requirements

* The application should read in data for customers and assign each customer an appointment with a teller.
* The application should output the following:
  * The total duration of all appointments for the teller with the longest total duration.
  * The total duration of all appointments for all tellers.
* A teller can have only one appointment at a time.
* When a customer's service type matches the specialty type of the assigned teller, the multiplier will be multiplied against the customer's appointment duration to reduce the appointment time.
* The customer's service type does not need to match the teller's specialty type (in fact, a customer's service type may not match any teller's specialty type).
* Not all tellers have the same multiplier, even within the same specialty type.
* Use the data set provided. DO NOT alter the JSON data.
* You may use any programming language.

### Result

Our goal is to process all customers AND have our tellers go home as early as possible. All the tellers will leave together once the last customer has been processed. Therefore, your results will not be measured according to the total time the tellers spend with the customers, but rather how long it takes for the last customer to be processed.

# Solution method
  1. Assign all the customers to tellers by types of the service and specialty(Type 1->Type 1, Type 2->Type 2, Type 3->Type 3, Type 4->Type 0)
    1.1 This gives us minimum The total duration of all appointments for all tellers but the time the last customer would be proccessed will be long
  2. Find mean time for all tellers to proceed customers
    2.1 This gives us the approximate time the last customer should pe proccessed
  3. Apply Algorithm to distribute customers between tellers from sorted list of tellers by total time spent on customers until the the teller's total-time spent close
    3.1 The teller who has the least total-time spent for customers gets customers from the teller who has the most total-time spent for customers until the difference in total-time spent for customers is <30( 1<->n, 2<->n-1, ...)
    3.2 Sort and repeat algorithm until the difference between teller who has the least total-time spent for customers gets customers from the teller who has the most total-time spent for customers until the difference in total-time spent for customers is <30
   
# Features to add 
  1. I would try to improve algorithm so that it would have less-time comlexity
 
    
