# Feline Strong :octocat:
This app is designed to plan and track fitness routines for Felines and humans.

## Links to Repositories and Deployed sites
- [Deployed Application](https://neuroplastic1.github.io/feline-strong-client/)
- [Client API Repository](https://github.com/Neuroplastic1/feline-strong-client)
- [Backend API URL](https://git.heroku.com/feline-strong-server.git)

## Technologies Used
- Python
- Django
- Postman
- cURL Scripts
- Heroku

## User Stories
- As a user, I can sign up
- As a user, I can sign in
- As a user, I can change my password
- As a user, I can sign out
- As a user, I can view all of my created Fitness Plans
- As a user, I can view a single Fitness Plan
- As a user, I can create a Fitness Plan
- As a user, I can edit a Fitness Plan
- As a user, I can delete a Plan


## Links to Entity Relation Diagram

 https://imgur.com/gallery/KKIucKN

## Planning and process
I started with planning and scetching wireframes.
 to create a model for a fitness plan for which I made a FItnessPlan class to crud on noted plans as one to many relationship to user. Each plan is only accessible by it's user.

 ## API Information
### Plans
| Verb   | URI Pattern  | Controller#Action  |
|:-------|:-------------|:-------------------|
| GET    | `/plans/`     | `plans#index`  |
| GET    | `/plans/:id` | `plans#show`   |
| POST   | `/plans`     | `plans#create` |
| PATCH  | `/plans/:id` | `plans#update` |
| DELETE | `/plans/:id` | `plans#destroy` |
