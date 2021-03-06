

## Lab 13:
- [ ] Install and configure the use of the pyramid_jwt library in your application, and configure the Pyramid policies and permissions for your views and routes
- [ ] You will need to configure your RootACL class in the project’s __init__.py file before your associated permissions on the routes/views will take effect
- In models/account.py:
- [ ] Refactor your Account model with a __init__ method, which allows your users password to be hashed by bcrypt before being stored in the database
- [ ] Create a check_credentials class method on your Account model which allows a verification of username and password, and returns None on validation failure or the Account instance on validation success
- In the views/ directory, create a new file called auth.py
- [ ] Add a new view controller class called AuthAPIView for defining your registration and login functionality
- [ ] You view controller should enable a post for registration and a get for login
- [ ] Each of these methods should construct and return a new JSON Web Token in the response, and Nothing else
- [ ] If the registration or login fails, handle those exceptions correctly with an appropriate status code and JSON response
- [ ] For example, if a user registers with an email that’s already registered in the system you will send a 409 Conflict status code with an appropriate message in the response body

## Lab 12: Model Relationships
- [x] Using the diagram below as a guide update your models/ directory with the new account.py, role.py, and associations.py files, and create each of the tables
- [ ] Ensure that your model relationships are functional
- [ ] Ensure that you’ve taken advantage of the SQLAlchemy relationship method to create additional functionality within your code base for accessing those new relationships
- [ ] Add your new models to the Initialization Script, drop and recreate your DB, and initialize again with your new tables


## Lab 11:
- [x] In your models/ directory, create a file called portfolio.py.
- You will create a Portfolio class with the following attributes:
- [x] id, name, date_created, date_updated
- [x] Define each attribute of your class with the appropriate data type and any further restrictions or definitions that each attribute should carry with it into the database table.
- Define two class methods on your Portfolio class:
- [x] one(): Retrieve a single instance from the database by the primary key for that record
- [x] new(): Create a single new instance of the Portfolio class
- In your models/ directory, create a file called stock.py.
- [x] You will create a Stock class with the following attributes, which are being defined to mirror the data that you will retrieve from your 3rd party API:
- [x] id, symbol, companyName, exchange, industry, website, description, CEO, issueType, sector, date_created, date_updated
- [x] Define each attribute of your class with the appropriate data type and any further restrictions or definitions that each attribute should carry with it into the database table.
- Define three class methods on your Stock class:
- [x] one(): Retrieve a single instance from the database by the primary key for that record
- [x] new(): Create a single new instance of the Stock class
- [x] destroy(): Remove a single instance from the database by the primary key for that record
- In your models/ directory, create a file called schemas.py for your model serializers.
- [x] You will define two Marshmallow schemas in this file, one for PortfolioSchema and one for StockSchema.
- In your views/portfolio.py file, you will further define the following View Class Controllers:
- [ ] PortfolioAPIView - Controller interactions with your Portfolio model/schema
- [ ] StockAPIView - Controller interactions with your Stock model/schema
- [ ] CompanyAPIView - 3rd-party API interactions for requesting company data for your portfolio
- You will be using the requests library and a free API from IEX TRADING, which does not require the use of an API key at this point. We are specifically interested in the Company Info and the Time Series info, both of which are accessible via an API call using a companies Stock Symbol.
- [ ] Using your model class methods, formulate an appropriate serialized response for each available endpoint / method that we configured in our last lab for this application. You may want to refer back to the LAB.md specification for each of those endpoints to review the functionality required.


## Lab 09: Deployment
- [ ] Deploy your API to AWS!


## Lab 08: Pyramid Web Framework
- [ ] Disable the unnecessary functionality of your scaffold, by commenting out the include() statements in your __init__.py:main() function; we will not be using Jinja2 templating (Delete that line) or Models for the time being
- [ ] Delete the templates/ directory
- [ ] Remove the contents of default.py and notfound.py
- Ensure that your application can accept requests to the following routes, and returns the appropriate response:
NOTE: You do not need to build any controller functionality other than a simple response with a status and JSON encoded message

- [ ] GET / - the base API route
    Status code: 200 OK
    Response body:
        GET / - the base API route
        POST /api/v1/auth/ - for registering a new account and signing up
        GET /api/v1/portfolio/{id}/ - for retrieving a user's portfolio
        POST /api/v1/stock/ - for creating a new company record
        GET /api/v1/stock/{id}/ - for retrieving a companies information
        DELETE /api/v1/stock/{id} - for deleting a company record
        GET /api/v1/company/{symbol} - for retrieving company detail from 3rd party API, where `{symbol}` is variable

- [ ] POST /api/v1/auth/ username=user password=seekret email=who@example.com - for registering a new account and signing up
    Status code: 201 CREATED
    Response body:
    {
        "username": "some user",
        //...
    }

- [ ] GET /api/v1/portfolio/{id}/ - for a user’s portfolio
    Status code: 200 OK
    Response body:
    {
        "portfolio": "dummy data",
        //...
    }

- [ ] POST /api/v1/stock/ name=data symbol=data portfolio_id=int ... - for creating a stock record associated with a user’s portfolio
    Status code: 201 CREATED
    Response body:
    {
        "company": "dummy data",
        //...
    }

- [ ] GET /api/v1/stock/{id}/ - for retrieving a stock record belonging to a user’s portfolio
    Status code: 200 OK
    Response body:
    {
        "company": "dummy data",
        //...
    }

- [ ] DELETE /api/v1/stock/{id}/ - for retrieving a stock record belonging to a user’s portfolio
    Status code: 204 NO CONTENT

- [ ] GET /api/v1/company/{symbol}/ - for retrieving company detail from 3rd party API, where {symbol} is variable
    Status code: 200 OK
    Response body:
    {
        "company": "dummy data",
        //...
    }
