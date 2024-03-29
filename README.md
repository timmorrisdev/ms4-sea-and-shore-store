# Sea & Shore Store

![Responsive Mockup of site](readme_assets/responsive_site.png)


# Project Synopsis

'Sea and Shore' is an e-commerce store focusing on watersports and outdoor pursuits equipment and clothing. The aim of the store is to encourage people to experience the great outdoors both safely and conveniently, all whilst keeping up-to-date with the latest fashions and trends. 

[//]: # ([See the live site here!]&#40;https://sea-and-shore-store.herokuapp.com/&#41;)

SITE NOT DEPLOYED SINCE STUDENT HEROKU ACCOUNT LAPSE - LOCAL DEMO ON REQUEST

This website is for educational purposes and checkout functionality is set up to accept stripe test card details. Please don't enter your personal card details.

To process a test stripe payment at checkout, please use the following details.

- card number : 4242 4242 4242 4242
- Any date
- Any CVV number

___
# User Experience (UX)

## User Stories

### Unregistered user goals

- As an unregistered user, I should be able to see what the store is selling and easily understand the kind of products on offer.
- As an unregistered user, I should be able to navigate through the website easily to explore the different features.
- As an unregistered user, I should be able to navigate through all the products sold in the store using clear and intuitive menus and categories.
- As an unregistered user, I should be able to search the product range.
- As an unregistered user, I should be able to sort any product results by price, rating, or brand.
- As an unregistered user, I should be able to add items to my basket and receive real-time, useful feedback when I interact with the website.
- As an unregistered user, I should be able to edit the items in my basket and receive feedback when something has changed.
- As an unregistered user, I should be able to check out as a guest user of the website.
- As an unregistered user, I should be able to receive email confirmation of my order. 
- As an unregistered user, I should be able to sign up and store my information to a personal profile in order to streamline future visits.

### Registered user goals

- As a registered user, I should be able to log in to my profile to make my experience more personal.
- As a registered user, I should be able save items to a wish-list for future purchase consideration. 
- As a registered user, I should be able to edit my default delivery and payment information. 
- As a registered user, I should be able to see and review my past orders.
- As a registered user, I should be able to rate and leave reviews for products on the site.
- As a registered user, I should be able to contact the business owner with any queries I might have.

### Admin

- As an admin user, I should be able to add, edit and delete items from the product range.
- As an admin user, I should have access to an admin section to see details of users and orders.
- As an admin user, I should be able to offer incentive to make larger purchases by offering free delivery over a set amount.


## Design

### Wireframes
- [Landing Page](https://github.com/timmorrisdev/ms4-sea-and-shore-store/blob/main/readme_assets/wireframes/Home%20page.png)
- [Product Page](https://github.com/timmorrisdev/ms4-sea-and-shore-store/blob/main/readme_assets/wireframes/Product%20Page.png)
- [Product Detail](https://github.com/timmorrisdev/ms4-sea-and-shore-store/blob/main/readme_assets/wireframes/Product%20Detail.png)
- [Shopping Bag](https://github.com/timmorrisdev/ms4-sea-and-shore-store/blob/main/readme_assets/wireframes/Shopping%20bag.png)
- [Checkout](https://github.com/timmorrisdev/ms4-sea-and-shore-store/blob/main/readme_assets/wireframes/Checkout.png)
- [User Profile](https://github.com/timmorrisdev/ms4-sea-and-shore-store/blob/main/readme_assets/wireframes/User%20Profile.png)
- [Wishlist](https://github.com/timmorrisdev/ms4-sea-and-shore-store/blob/main/readme_assets/wireframes/Wishlist.png)
- [Add / Edit Product](https://github.com/timmorrisdev/ms4-sea-and-shore-store/blob/main/readme_assets/wireframes/Add_Edit%20Product.png)
- [Add / Edit Review](https://github.com/timmorrisdev/ms4-sea-and-shore-store/blob/main/readme_assets/wireframes/Add%20review.png)


### Colour Scheme
 - I chose an image for the home page that would be both visually beautiful, and convey the purpose of the site to the user. Then throughout the site I chose to keep the colour scheme neutral. Using contrasting black and white elements to create a clean, modern feel and user experience. 


### Fonts
- I chose Montserrat from google fonts for the site as it gives good readability and has a modern aesthetic.


## Data Models and Schema
### Models
 - Products App
    - Product: Holds the information for each individual product.
    - Category: Holds the available categories for the products.
    - Product Variations: Any variations of a specific product (sizes etc)

- Checkout App
    - Order: Holds the order information and details of the customer who placed it.
    - Order Line Item: Each item within a specific order. 

- User
    - Created with django allauth containing the customer username, email and password.

- User Profile App
    - User Profile: Holds user default delivery information

- Wishlist App
    - User Wishlist: Holds any items a specific user places into a wishlist.

- Product Review App
    - Holds any reviews added for a specific product. Details the user that left each review.

### Database Diagram

This is a diagram of the database show the relations between each model. It was made using [dbdiagram.io](https://dbdiagram.io/).

![Diagram of the database](/readme_assets/SeaShore_DBdiagram.png)

## Features

### Home Page
- Overview
    - Large 'hero' image is visually striking as well as providing the user with context to the kind of store it is.
    - Clear navigation and streamlined design make it easy for the user to make decisions about their journey through the site.

    ![Home Page Overview](readme_assets/features_screengrabs/home_page/home_page.png)



- Navigation and Search
    - Search function for all products and navigation links with drop-down menus for each category 'group'. 

    ![Home Page Navigation](readme_assets/features_screengrabs/home_page/home_navigation.png)

- Site Feature Icons
    - Clear, bold icons to allow the user to navigate user and shopping bag features.

    ![Site feature Icons](readme_assets/features_screengrabs/home_page/info_icons.png)

- Browse Button
    - Main 'onward-journey' prompt for the user if they are not looking for a specific product using the navigation or search.

    ![Browse Button](readme_assets/features_screengrabs/home_page/browse_button.png)


### Products Page

- Overview
    - Product page displays summary cards for relevant products dependent on criteria entered by the user. Either search parameter or category navigation.

    ![Product Page Overview](readme_assets/features_screengrabs/products_page/products_page_overview.png)

- Product Summary Card
    - Summary of product while user is browsing. Delivers an overview of the product details including image, name, price, rating, and wishlist status via star icon.

    ![Product Summary Card](readme_assets/features_screengrabs/products_page/product_summary.png)

- Search Result Feedback
    - The user is provided detail of how many products they are currently viewing based on their criteria.

    ![Search Results Feedback](readme_assets/features_screengrabs/products_page/search_result_feedback.png)

- Sort Selector
    - Dropdown menu allowing the user to determine the ordering of the products they are viewing to make the results meet their needs more easily.

    ![Sort Selector](readme_assets/features_screengrabs/products_page/sort_dropdown.png)

- Pagination
    - This area of the site uses the pagination feature included in the ListView class based view in Django. It allows the user to navigate their search results in a more manageable way.

    ![Pagination](readme_assets/features_screengrabs/products_page/pagination.png)


### Product Detail Page

- Product Details Section
    - Provides the user with a detailed overview of the specific product. 
    - Product rating uses the average of any ratings issued in product reviews and is calculated in the product review app views.
    - Includes the buttons and menus for the user to select a specific size (if applicable) and add a defined quantity of the item to the shopping bag.
    - 'Star' icon informs the user if the product is in their wishlist and acts as a toggle button to add / remove it to the wishlist.

    ![Product Detail Section](readme_assets/features_screengrabs/product_detail_page/product_details_section.png)

- Products Review Section
    - Displays any user reviews for the specific product.
    - If the user in logged in, the 'add review' link is available and active.
    - Edit / Delete buttons available to the review author. 

    ![Product Review Section](readme_assets/features_screengrabs/product_detail_page/product_review_seciton.png)

- Add Product Review
    - If the user is logged in and has clicked to add a review to a product, the following form page will be displayed. 
    - The same form is displayed for a user to edit a review, pre-populated with the review data being edited.

    ![Add Review Page](readme_assets/features_screengrabs/add_review_page/add_review_page.png)

- Shopping Bag Page
    - Displays the details of all items in the users shopping bag.
    - Offers the ability to update item quantity, or remove an item from the shopping bag.
    - Displays bag total and shipping fees, if the user has not met the free delivery threshold.
    - Navigation buttons to either checkout, or keep shopping.

    ![Shopping Bag](readme_assets/features_screengrabs/shopping_bag/shopping_bag_page.png)

- Checkout Page
    - Prompts the user to input their shipping and payment information.
    - Displays order summary.

    ![Checkout Page](readme_assets/features_screengrabs/checkout_page/checkout_page.png)

    - Allows the user to save the information being entered to their profile if they are registered and logged in.

    ![Save User Info](readme_assets/features_screengrabs/checkout_page/save_info.png)

    - Upon successful checkout, user is redirected to a success page with an overview of the order and the shipping information.

    ![Order Confirmation](readme_assets/features_screengrabs/checkout_page/order_confirmation.png)

- User Profile
    - Displays the users default information to be pre-populated at checkout and offers the ability to edit.
    - Order history gives an overview of any orders placed. User can click an order to display the order confirmation for the past order.

    ![User Profile Page](readme_assets/features_screengrabs/profile_page/profile_page.png)

- Wishlist Page
    - If user has added items to their wishlist, the product summary card for each item is displayed.

    ![User Wishlist](readme_assets/features_screengrabs/wishlist_page/wishlsit_page.png)

    - If the user has not added any items to the wishlist, the page will display feedback to  reflect this.

    ![No Wishlist Items](readme_assets/features_screengrabs/wishlist_page/no_items.png)

- Admin Product Management
    - Add product form for admin to input a new product to the store.
    - If 'has variations' is selected, submitting the form will redirect the admin to add variations of the product.

    ![Add Product Form](readme_assets/features_screengrabs/product_management/add_product.png)

    - Add product variations page displays existing variations and offers the admin the ability to add additional variations as well as edit and delete existing variations.

    ![Add Product Variations](readme_assets/features_screengrabs/product_management/add_variation.png)

    - Edit existing product form.
    - Pre-populated with current product details.
    - Displays any product variations and displays link to manage.

    ![Edit Product](readme_assets/features_screengrabs/product_management/edit_product.png)

- Allauth Registration, Sign In and Sign Out
    - Registration page.
    - User is required to confirm email address using a link in an automated email sent to the provided address.

    ![Registration Page](readme_assets/features_screengrabs/allauth/sign_up.png)

    - Sign In page

    ![Sign In Page](readme_assets/features_screengrabs/allauth/sign_in.png)

    - Sign Out Page

    ![Sign Out Page](readme_assets/features_screengrabs/allauth/sign_out.png)

- Django Messages
    - The user is given feedback on any action taken on the site via django message popups using Bootstrap toasts.
    - Item successfully added to bag.

    ![Add to bag](readme_assets/features_screengrabs/messages/add_bag_message.png)
    
    - Order confirmation

    ![Order confirmation](readme_assets/features_screengrabs/messages/order_confirmation_mesaage.png)

    - Item successfully added to wishlist.

    ![Wishlist Add](readme_assets/features_screengrabs/messages/wishlist_messge.png)



### Other Features
- Responsive across all devices and screen sizes.
- Adaptive to modify content shown to be appropriate for user device or screen size.

### Future Development Opportunities

- A blog to allow the business owner to publish posts about real-world product testing and to be able to interact with customers via a comments section.

- For the admin to be able to offer 'recommended products' to registered users based on past purchases in their order history.


___
# Technologies Used
## Languages Used
- [Python3](https://www.python.org/downloads/)
- [JavaScript](https://www.javascript.com/)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [HTML5](https://en.wikipedia.org/wiki/HTML5)

## Django and Associated Extensions

- [Django](https://www.djangoproject.com/)
    - Django was was used to create the project and code infrastructure. Django templating language was used when passing data between the Front-end and Back-end.

- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
    - Allauth was used to create user registration and login functionality.

- [Django Countries](https://pypi.org/project/django-countries/)
    - Django Countries was used for formatting of the 'Country' field in the checkout form and in the default user info within the profile section.

- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
    - Used to format the default django form fields across the site.


- [Django Coverage](https://pypi.org/project/django-coverage/)
    - Used to monitor coverage of automation testing written for the product, product_review and wishlist apps.


## Frameworks, Libraries & Programs Used

- [jQuery](https://jquery.com/)
    - jQuery was used across the site when additional steps were needed to pass appropriate data to the back end, as well as when overriding some of the default behaviours and styling of django elements
    - jQuery was also used as part of Bootstrap and is used for Javascript plugins such as the modals.

- [Heroku](https://www.heroku.com/)
    - Heroku was used to deploy the site. The Heroku Postgres add-on was also used to create the production database for the project.

- [Stripe](https://stripe.com/gb)
    - Stripe was used to handle payments made on the site. Stripes webhooks were also used to offer payment backup in the event of payment failure. 

- [AWS(Amazon Web Services)](https://aws.amazon.com/)
    - Amazon Web Services was used to host the static files and media files used by the site.

- [Google Fonts](https://fonts.google.com/)
    - Google Fonts was used to import the 'Montserrat' font, which was used throughout the site.

- [Font Awesome](https://fontawesome.com/)
    - Used to source icons used across the site.

- [Git](https://git-scm.com/)
    - Git was used for version control using the terminal in Gitpod to 'add' and 'commit' to Git and to push changes to the GitHub repository using 'git push'.

- [Gitpod](https://gitpod.io/)
    - Gitpod.io was used as the primary development environment when coding for the site. It's terminal was used to preview the site via temporary server, and for version control using Git commands.

- [Github](https://github.com/)
    - GitHub was used to store the code pushed from Gitpod and as deployment for the [published site.](https://sea-and-shore-store.herokuapp.com/)

- [Balsamiq](https://balsamiq.com/)
    - Balsamiq was used to create the wireframes for the site while in the 'skeleton' stage of my UX process.

- [Autoprefixer](http://autoprefixer.github.io/)
    - Autoprefixer was used in the final stage of development to parse CSS code and add vendor prefixes.

- [Am I Responsive?](http://ami.responsivedesign.is/#)
    - Used to check responsiveness across different device sizes. 

___

# Deployment

The project was deployed to Heroku and can be found [here](https://sea-and-shore-store.herokuapp.com/).

The following steps were taken throughout the project to achieve deployment of the live site.

## Create Github Repository

- The repository was created using the green 'new' button on [Github](https://github.com/) and selecting the Code Institute Full Template from the dropdown menu. 
- Once created I was able to open the repository in Gitpod using the installed extension. From this point on, the command line in Gitpod was used for version control with git add, commit and push commands.


## Create Django Application
In the terminal type the following commands to create and initialise the project:
    
- Install Django
    ```
    pip3 install django
    ```

- Create project-level application
    ```
    django-admin startproject [project_name] .
    ```

- Create Superuser to access the Django admin panel. Follow the prompts to input a username, email and password.

Note: This step will be repeated when deploying to Heroku and migrating the database to Postgres.

    ```
    python3 manage.py createsuperuser
    ```
- Install apps to implement site features.

    ```
    python3 manage.py startapp [app_name]
    ```

## Deployment to Heroku

In order to deploy the app via [heroku](https://dashboard.heroku.com/apps), the following steps must be taken. 

### Heroku
- Navigate to [heroku](https://heroku.com/) and create a new app in your dashboard.

- Assign an app name and region and hit 'create app'.

- Navigate to the resources tab from the app dashboard, search for Postgres and select to add to the project.

### Django

- To use Postgress, install the following packages.

    ```
    pip3 install dj_database_url
    ```
    ```
    pip3 install psycopg2_binary
    ```
- Add the packages to the requirements.txt file using the following command.

    ```
    pip3 freeze > requirements.txt
    ```

- In settings.py:
    - import dj_database_url.

    ```python
    import dj_database_url
    ```
    - Replace settings for the development database with the following code. Note that the database url is obtained using an environment variable set up in Heroku to avoid exposing the database when pushing to Github. The database settings were also placed in a conditional statement to allow use of development database if necessary.

    ```python
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default':dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
    ```

- Create fixtures files to be installed in the new database. For my project I required data already added for the Product, Category and ProductVariation models.
    ```

        python3 manage.py dumpdata products.Product > products.json

        python3 manage.py dumpdata products.Category > category.json

        python3 manage.py dumpdata products.ProductVariations > product_variations.json
    ```

- Migrate the project models to database.
    ```
    python3 manage.py migrate
    ```

- Use the created fixtures files to add the product data to the database. Note that the order is important to allow model relationships to be made correctly.

    ``` 
    python3 manage.py loaddata category
    python3 manage.py loaddata products
    python3 manage.py loaddata product_variations
    ```
- Create superuser for the production database and admin panel. Follow the prompts to input a username, email and password.

    ```
    python3 manage.py createsuperuser
    ```

- The Postgress database is now set up and configured.

- Install Gunicorn and create Procfile.
    ```
    pip3 install gunicon
    ```
    ```
    touch Procfile
    ```
- Within the Procfile, place the following code.
    ```
    web: gunicorn sea_and_shore.wsgi:application
    ```

- Login to Heroku and prevent static files being collected until AWS is setup.
    ```
    heroku login -i
    ```
    ```
    heroku config:set DISABLE_COLLECTSTATIC=1 --app <app name>
    ```

- Add Heroku to the allowed hosts in settings.py. 'Localhost' is kept in place for use in future development.
    ```python
    ALLOWED_HOSTS = ["[heroku_app_name].herokuapp.com", "localhost"]
    ```

- Set up remote to Heroku app and push files to Heroku.
    ```
    heroku git: remote -a [heroku_app_name]
    ```
    ```
    git push heroku main
    ```

- On Heroku.com, navigate to the deploy tab of the app dashboard to locate the project Github repository and enable automatic deployment from future pushes to Github.

### Amazon Web Services (AWS)

Amazon Web Services was used to host the static files and media files for the site.

- Follow the steps on the [AWS website](https://aws.amazon.com/) to create a new account and sign in.

- Search for and navigate to the S3 service and follow the following steps to create a new 'bucket'
    - In the S3 dashboard, click the 'create bucket' button.
    - Give the bucket a name, select the region nearest to your location and un-check the 'block public access' settings checkbox.
    - Hit 'create bucket'

- Configure the properties for the bucket.
    - In the properties tab of the bucket, navigate to the 'Static website hosting' section and click edit.
    - Enable Static website hosting using the checkbox.
    - Input the default index and error documents as 'index.html' and 'error.html'.
    - Save changes.

- Configure the permissions for the bucket.
    - In the permissions tab of the bucket.
    - Select edit in the Cross-origin resource sharing(CORS) section and
     pPaste the following code into the CORS configuration section.
    ```
    [
        {
            "AllowedHeaders": [
                "Authorization"
            ],
            "AllowedMethods": [
                "GET"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": []
        }
    ]
    ```
    - Back in the permissions menu, hit edit on the bucket policy section and select 'generate policy'.
        - Select policy type of 'S3 bucket policy'
        - Allow all principles by entering a '*' in the Principal field.
        - Select 'get object' from the action dropdown.
        - Copy the 'arn' from the edit bucket policy page and paste into the Amazon Resource Name (ARN) field.
        - Click 'add statement'
        - Click generate policy and copy the code.
        - Paste the code into the policy field in the edit bucket policy section, adding a '/*' to the resource line.
        - Hit save.
    

    - Navigate to the 'edit access control list (ACL) section and grant 'list' access for everyone by selecting the checkbox.

- Create a user to access the S3 bucket using IAM.
    - Navigate to the IAM page from the AWS dashboard.
    - Create group.
        - Select 'group' from the menu and click to create a new group, following the instructions to name and then create.
    - Create policy
        - Select 'policies' from the menu and click 'create policy'.
        - Select the 'JSON' tab and click 'import managed bucket'.
        - Search for, and import the 'S3 full access' policy.
        - Copy the ARN from the bucket policy section and paste this in as the 'Resource' value.
        - Click 'review policy' and give it a name and description and hit 'create policy.
    - Add policy to group.
        - Navigate to the groups menu and select the group.
        - Click 'attach policy', search for the newly-created policy from the previous step.
        - Select the policy using the checkbox and click 'attach policy'
    - Create user
        - Select 'users' from the menu and click 'add user'.
        - Name the user and grant programatic access using the checkbox.
        - Select the group created in the previous steps.
        - Click through to the end of the options and click 'create user'
        - Download and save the user CSV file.

- Connect Django to S3
    - Install packages Boto3 and Django storages and add to our requirements.txt file.
    ```
    pip3 install boto3
    ```
    ```
    pip3 install django-storages
    ```
    ```
    pip3 freeze > requirements.txt
    ```
    - Add 'storages' to the installed apps in settings.py.
    - Add the following settings to settings.py. Note the 'USE_AWS' environment variable will be added to Heroku to allow use of AWS only when desirable.
    ```python
    if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = '[bucket name]'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    ```
    - Add the environment variables 'AWS_ACCESS_KEY_ID' and 'AWS_SECRET_ACCESS_KEY' to Heroku with the values found the user CSV file downloaded from the AWS setup.

    - Create custom_storages.py at the top-level of the project and input the locations for Django to store the files.
    ```python
    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage


    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION


    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION
    ```

- With all these settings complete, remove the 'DISABLE_COLLECTSTATIC variable from Heroku and AWS is ready to use.

- Add media to AWS
    - Navigate to the S3 bucket on the AWS site.
    - Click to create a new folder and name it 'media'
    - Within the folder, click the button to upload files and add any relevant site media.
    - Under permissions, select to grant public read access.
 


## Forking the repository in GitHub
Forking the repository creates a copy of the original repository in your own account to allow changes to be made without affecting the original repository.
1. Log in to GitHub and navigate to the GitHub repository page [here](https://github.com/timmorrisdev/ms4-sea-and-shore-store).
2. In the top-right of the page, below the user avatar, locate the "fork" button.
3. Click the "fork" button and you should now have a copy of the repository in your own account. 

## Making a Local Clone
Details of how to make a local copy of the GutHub repository can be found [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository). To clone using HTTPS follow these steps.
1. Navigate to the GitHub repository [here](https://github.com/timmorrisdev/ms4-sea-and-shore-store).
2. Click the "Code" drop-down menu above the list of files.
3. Copy the HTTPS address to the clipboard using the button provided.
4. Open Terminal.
5. Change the current directory to the location you wish to copy the directory.
6. Type 'git clone' and then paste the HTTPS url you copied earlier. 
7. Press enter and your local clone will be created. 


___
# Testing
## Responsiveness Testing
I used google dev tools throughout the development process to check responsiveness across different screen sizes. 

I was also sure to deploy the site to Heroku early in development to allow for review of the live site on various devices throughout the process.

## W3C Markup, CSS Validation & JSHint Validation
I used the W3C Markup, CSS Validator and JSHint Validator Services to check and validate each page throughout the site to check for errors. 
### [Markup Validation Service](https://validator.w3.org/)
The HTML code on the site passed through the validator showing errors to do with the implementation of the Django templating language.

### [CSS Validation Service](https://jigsaw.w3.org/css-validator/)
My CSS files across the site passed through the w3 validator with no errors.

### [JSHint Validation Service](https://jshint.com/)
My JavaScript files across the site passed through the validator with no errors. 

### [PEP8 check](http://pep8online.com/)
Across the site, the code is PEP8 compliant.

## Automation Unit Testing
Due to time restrictions, automation unit tests were written for select apps within the project.

The following areas of the application were tested abd Django Coverage was used to ensure all code was included.

- Products app.
    - models.py
    - views.py
    - urls.py

- Product Reviews app.
    - models.py
    - views.py
    - urls.py

- Wishlist app.
    - models.py
    - views.py
    - urls.py

## Lighthouse Testing

I ran lighthouse testing across each area of the site. The results and details of any issues resolved are below.

### Index.hmtl
- Accessibility issue relating to 'a' element label duplication. Most likely an oversight when copying the navigation dropdown menus for category browsing.

![Lighthouse Index.html](readme_assets/lighthouse_tests/lighthouse_index.png)

### Products.html

![products.html](readme_assets/lighthouse_tests/lighthouse_products.png)

### Product_detail.html

- Missing label for quantity input.
- Missing names on decrement and increment buttons in quantity section.

![product_detail.html](readme_assets/lighthouse_tests/lighthouse_product_detail.png)

### Bag.html

- Missing label for quantity input.
- Missing names on decrement and increment buttons in quantity section.

![bag.html](readme_assets/lighthouse_tests/lighthouse_bag.png)

### Checkout.html

![checkout.html](readme_assets/lighthouse_tests/lighthouse_checkout.png)


### Checkout_success.html

![checkout_success.html](readme_assets/lighthouse_tests/lighthouse_checkout_success.png)

### Profile.html

![profile.html](readme_assets/lighthouse_tests/lighthouse_profile.png)

### Wishlist.html

![wihslist.html](readme_assets/lighthouse_tests/lighthouse_wishlist.png)

### Add_product_review.html

![wihslist.html](readme_assets/lighthouse_tests/lighthouse_review.png)

### Add_product.html
- Unresolved accessibility issues with image field generated with the 'custom clearable file input' widget.

![add_product.html](readme_assets/lighthouse_tests/lighthouse_add_product.png)

### Edit_product.html
- Unresolved accessibility issues with image field generated with the 'custom clearable file input' widget.

![edit_product.html](readme_assets/lighthouse_tests/lighthouse_edit_product.png)

### Add_product_variation.html
- Unresolved accessibility issues with image field generated with the 'custom clearable file input' widget.

![add_product_variation.html](readme_assets/lighthouse_tests/lighthouse_variations.png)


## Testing UX User Stories

### Unregistered user goals
- As an unregistered user, I should be able to see what the store is selling and easily understand the kind of products on offer.
    - The home page clearly outlines the type of product range available to the customer via the category menu headings, the store name, and store 'ethos' heading.

        ![User Story 1](readme_assets/user_story_images/1_ethos.png)

    - The hero image gives a clear idea to the user the ethos of the store.

        ![User Story 2](readme_assets/user_story_images/2_hero_image.jpg)

- As an unregistered user, I should be able to navigate through the website easily to explore the different features.
    - Features and areas of the site are clearly labelled throughout with the assistance of recognised icons to represent different features and links.

        ![User Story 3](readme_assets/user_story_images/3_features_of_site.png)

- As an unregistered user, I should be able to navigate through all the products sold in the store using clear and intuitive menus and categories.
    - Categories are clearly laid out.

        ![User Story 4](readme_assets/user_story_images/4_categories.png)

- As an unregistered user, I should be able to search the product range.
    - Search functionality available from any location on the site.

        ![User Story 5](readme_assets/user_story_images/5_search.png)

- As an unregistered user, I should be able to sort any product results by price, rating, or brand.
    - The sort dropdown on the products page allows for users to order products.

        ![User Story 6](readme_assets/user_story_images/6_sort.png)

    - Individual brands can be browsed using the main navigation dropdown.\

        ![User Story 7](readme_assets/user_story_images/7_brands.png)

- As an unregistered user, I should be able to add items to my basket and receive real-time, useful feedback when I interact with the website.
    - Adding items to the basket can be done as an unregistered user.

        ![User Story 8](readme_assets/user_story_images/8_bag.png)

    - Message 'toasts' are displayed whenever there is meaningful user interaction with the site.

        ![User Story 9](readme_assets/user_story_images/9_toast.png)

- As an unregistered user, I should be able to edit the items in my basket and receive feedback when something has changed.
    - The bag page allows users to edit quantity or remove items from shopping bag.

        ![User Story 10](readme_assets/user_story_images/10_qty.png)

- As an unregistered user, I should be able to check out as a guest user of the website.
    - Unregistered users are able to checkout and complete a purchase.

        ![User Story 11](readme_assets/user_story_images/11_checkout.png)

- As an unregistered user, I should be able to receive email confirmation of my order. 
    - Automated emails are sent to the user-provided address upon checking out.

- As an unregistered user, I should be able to sign up and store my information to a personal profile in order to streamline future visits.
    - User registration available throughout the site.

        ![User Story 12](readme_assets/user_story_images/12_register.png)

    - Prompt via checkbox to store user information on checkout.

        ![User Story 13](readme_assets/user_story_images/13_prompt.png)

### Registered user goals

- As a registered user, I should be able to log in to my profile to make my experience more personal.
    - Users can log in and view their profile.

        ![User Story 14](readme_assets/user_story_images/14_profile.png)

- As a registered user, I should be able save items to a wish-list for future purchase consideration. 
    - Wishlist status of items clear displayed for each product and wishlist creation is automatic upon user input.

        ![User Story 15](readme_assets/user_story_images/15_wishlist.png)

- As a registered user, I should be able to edit my default delivery and payment information. 
    - User can edit information on their profile page. 

        ![User Story 16](readme_assets/user_story_images/16_update.png)

- As a registered user, I should be able to see and review my past orders.
    - Past orders are displayed on the user profile page.

        ![User Story 17](readme_assets/user_story_images/17_order_history.png)

- As a registered user, I should be able to rate and leave reviews for products on the site.
    - Product ratings are clearly displayed and leaving a review for a proudct is available to any user who is logged in.

        ![User Story 18](readme_assets/user_story_images/18_reviews.png)


### Admin user goals

- As an admin user, I should be able to add, edit and delete items from the product range.
    - Superusers of the site can access CRUD functionality for products directly via the site, or via the django admin panel.

        ![User Story 19](readme_assets/user_story_images/19_add_product.png)

        ![User Story 20](readme_assets/user_story_images/20_add_product_admin.png)

- As an admin user, I should have access to an admin section to see details of users and orders.
    - Superusers of the site can log in to the django admin panel to see details.

        ![User Story 21](readme_assets/user_story_images/21_full_admin.png)

- As an admin user, I should be able to offer incentive to make larger purchases by offering free delivery over a set amount.
    - A 'free delivery threshold' can be set and clearly displayed to the user.

        ![User Story 22](readme_assets/user_story_images/22_site_delivery.png)

        ![User Story 23](readme_assets/user_story_images/23_settings_delivery.png)


## Peer Code Review

I posted this project on the Code Institute 'peer-code-review' channel and also to a London coders group comprised of both students and Code Institute alumni.

The followiung issues were raised.

- Pagination navigation styling on smaller devices.

    - Buttons sizing inconsistent when content wrapping to multiple lines.

        ![pagination problem](readme_assets/peer_review/pagination_problem.png)
    
    - Issue resolved using HTML. Content wrapped in 'small' tags and some words hidden on smaller screen while functionality still remaining clear to the user.

        ![pagination solution](readme_assets/peer_review/pagination_solution.png)

- 'Back to top' button not functioning on checkout page.

    - Button overlapping with product quantity links, causing the button not to function.

        ![back to top problem](readme_assets/peer_review/back_to_top_problem.png)
    
    - Issue resolved using CSS to add padding the container holding the product overview and allow the buttons spacing to function as expected.

        ![back to top solution](readme_assets/peer_review/back_to_top_solution.png)

- Allauth user account interaction area obscured.

    - Login, logout, register input sections were obscured by the top nav section.

        ![allauth problem](readme_assets/peer_review/allauth_problem.png)
    
    - Issue resolved using CSS to add top margin to the container displaying the account sections.

        ![allauth solution](readme_assets/peer_review/allauth_solution.png)

## Cross-Browser/Device Testing
I tested the site across multiple devices using different browsers.
- Browsers tested
    - Chrome
    - Safari
    - Firefox

- Devices tested
    - Mac Pro w/ Dell 24 inch monitor
    - Macbook Pro 15 inch
    - iPhone 12
    - iPad air 2

## Known Bugs / Issues

___
# Credits
## Code

- The code and concept for this project is based around the 'Boutique Ado' learning walkthrough project by the Code Institute.
- The following youtube videos were used as additional learning for aspects of the code.
    - [Very Academy ecommerce wishlist](https://www.youtube.com/watch?v=OgA0TTKAtqQ)
    - [Just Django Class Based views](https://www.youtube.com/watch?v=S1wMmFFefRM)
    - [Coding Point ecommerce walkthrough](https://www.youtube.com/watch?v=UjisbVs6gww)
    - [Dennis Ivanov Class Based views](https://www.youtube.com/watch?v=RE0HlKch_3U)
    - [Corey Schafer Decorators](https://www.youtube.com/watch?v=FsAPt_9Bf3U)
    - [Very Academy automation testing series](https://www.youtube.com/watch?v=swEjbCW9XDY)
- [Stack Overflow](https://stackoverflow.com/) was used extensively when problem solving. Specifically the following threads.
    - [Check if image url exists](https://stackoverflow.com/questions/10543940/check-if-a-url-to-an-image-is-up-and-exists-in-python)
    - [Add wishlist](https://stackoverflow.com/questions/56580696/how-to-implement-add-to-wishlist-for-a-product-in-django)
    - [Specify login required redirect](https://stackoverflow.com/questions/3578882/how-to-specify-the-login-required-redirect-url-in-django)
    - [Select distinct values from table field](https://stackoverflow.com/questions/2466496/select-distinct-values-from-a-table-field)
    - [Redirect to same page after POST request](https://stackoverflow.com/questions/39560175/redirect-to-same-page-after-post-method-using-class-based-views)

- The [Django documentation](https://docs.djangoproject.com/en/4.0/) was used a lot while working on the project. Especially when researching class based views.

## Content

- Product information taken from the existing ecommerce store [Surfdome](https://www.surfdome.com/).

## Media

- Product images downloaded from [Surfdome](https://www.surfdome.com/) ecommerce store.
- Background image by [Will Truettner from unsplash](https://unsplash.com/photos/Rk-JT2OypZA).

## Acknowledgements
- Thank you to my mentor, Rohit Sharma for all your guidance and support.
- Thank you to the Code Institute tutor support and Slack community for all the help throughout this project.
