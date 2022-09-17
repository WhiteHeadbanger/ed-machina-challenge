# ed-machina-challenge
I hope you don't mind but I tend to code and write about coding in english, although there are a few code commentaries that are in spanish, for simplicity.
 The project uses models of the tables, with their respective schemas, a routes file with the endpoints and their logic. I was hoping to include FrontEnd views, as I was designing this with an MVC approach initially.
 Please, look at the comments in the routes.py file. I had encountered a few errors that I couldn't solve. 
 
 
# How to run
```shell
git clone https://github.com/WhiteHeadbanger/ed-machina-challenge.git
cd ed-machina-challenge
docker-compose up
```

# Endpoints
```
POST /create
```
Creates a new Lead. Accepts a body request. You can find an example of what it should look down below.

```
GET /leads/<int:id>
```
Returns a Lead by id.

```
GET /leads
```
Returns the loaded Leads, paginated. 

# Example of body request

```json
{
    "lead_name":"John Doe",
    "email":"email@example.com",
    "address":"False Street 1234",
    "phone":55555555,
    "inscription_year":2022,
    "careers":[
        {
            "career_name":"Ingenieria en Sistemas",
            "courses":[
                {
                    "course_name":"Analisis Matematico I",
                    "course_time":60,
                    "course_times_quantity":1
                },
                {
                    "course_name":"Fisica II",
                    "course_time":240,
                    "course_times_quantity":1
                },
                {
                    "course_name":"Sistemas Operativos",
                    "course_time":120,
                    "course_times_quantity":5
                }
            ]
        },
        {
            "career_name":"Ingenieria en Electronica",
            "courses":[
                {
                    "course_name":"Electronica I",
                    "course_time":100,
                    "course_times_quantity":2
                },
                {
                    "course_name":"Laboratorio I",
                    "course_time":320,
                    "course_times_quantity":4
                }
            ]
        }
    ]
}
```

If a get request is made to /leads/[id], you should be able to see a similar response to the request.
