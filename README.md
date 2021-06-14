Welcome! [github.com](https://github.com/GiovanniSalvi/World_Wide_Wine)

# UX

## I realized this project as part of the Full Stack Frameworks with Django module that I am attending at "code academy" training course.

### The App 

### 

### The nav menu, home-button and accounts icons  are repeated in all site's pages to get app style consistent.


---


## Project's Mockup screenshots

* [Homepage]()

* [Stock]()

* [Checkout]()

* [Cart]()

* [Register]()

* [Login]()

* [Checkout Success]()

* [About]()

* [Newsletter]()

---

## Features:

### Existing features

* Feature1: Registration Form

* Feature2: Login Form

* Feature3: Search tab, Navbar

* Feature4: Cart

* Feature5: Checkout

* Feature6: Stripe Payments

* Feature7: List of products

* Feature8: Reset Password

* Feature9: Add,Edit and Delete Products

### Features left to implement

* Update/Remove Account

* Toast

* Webhooks

* Order History

* Newsletter

---

# Technology used:

## Programming languages

* HTML

* CSS

* JAVASCRIPT

* PYTHON3 + DJANGO

### Libraries

* [Bootstrap.com](https://getbootstrap.com/)

* [jQuery](https://jquery.com/)

---

## Testing

### In order to navigate easily through the site:

* The homepage provides an header with the [cart and account icons](https://user-images.githubusercontent.com/61980577/121951358-bd303e80-cd52-11eb-9e0a-f30f7100595b.png),a [navbar](https://user-images.githubusercontent.com/61980577/121951355-bc97a800-cd52-11eb-9e10-1b8734ae9af7.png) to navigate through the app.The main section is displayed an hero image, a brief decription of the products features on sale and a link to all wines in stock.

* Account icon dropdown menu provides a [registration](https://user-images.githubusercontent.com/61980577/121951375-c3261f80-cd52-11eb-9034-aec5f79ca575.png) and a [login](https://user-images.githubusercontent.com/61980577/121951368-c1f4f280-cd52-11eb-9e55-44ec369b29f4.png) if user is already signed up.

* Clicking on ['clickhere'](https://user-images.githubusercontent.com/61980577/121951401-c9b49700-cd52-11eb-93bb-522a988948b5.png) button in the homepage leads to the whole stock of products on sale in the site(stock page).The products are displayed in three rows and are wrapped in a [card container](https://user-images.githubusercontent.com/61980577/121951400-c91c0080-cd52-11eb-8058-f8db0e611d5a.png).Name, image, price and the country where wine is produced are displayed inside the card.

* Clicking on wine's name inside the card leads to a page containing [wine's details](https://user-images.githubusercontent.com/61980577/121951399-c8836a00-cd52-11eb-8337-8c2d12afe3b6.png) and a brief description of the product.For site administrator is possible to update the stock deleting or editing the selected product clicking on ['delete'](https://user-images.githubusercontent.com/61980577/121951396-c8836a00-cd52-11eb-8769-536086becc01.png) or ['edit'](https://user-images.githubusercontent.com/61980577/121951395-c8836a00-cd52-11eb-8c33-6c8301f6e5b2.png) buttons just below wine's details.

* The two button at the bottom of products details page are ['keep shopping'](https://user-images.githubusercontent.com/61980577/121951395-c8836a00-cd52-11eb-8c33-6c8301f6e5b2.png) button to redirect users to the stock page and [add to cart](https://user-images.githubusercontent.com/61980577/121951394-c7ead380-cd52-11eb-87fe-3ece4b5806a5.png) button in order to add the products in the bag.Clicking on the cart icon  with the amount of the order updated, shown below the icon[0.00$](https://user-images.githubusercontent.com/61980577/121951382-c6211000-cd52-11eb-87fd-ecd6d2c4ed01.png), leads to the [cart page](https://user-images.githubusercontent.com/61980577/121951392-c7ead380-cd52-11eb-9465-efa61b1cd6c5.png).['Checkout'](https://user-images.githubusercontent.com/61980577/121951391-c7523d00-cd52-11eb-90e9-da23d68d1e76.png) button in the cart page allow the users to complete the checkout leading to a  form to fill with the required users details.

* Checkout page provides a [form](https://user-images.githubusercontent.com/61980577/121951389-c7523d00-cd52-11eb-8f86-bc4e22a657d8.png) to fill in order to complete the purchase.Field required are full-name, an email address,country,city,phone number and a postal code for the delivery.Below the form, stripe payment details [inputs](https://user-images.githubusercontent.com/61980577/121951387-c7523d00-cd52-11eb-90cc-3a2b2e78f3b8.png) such card number,ccv , card expiration date and a zip code are displayed.Only authenticated users are allowed to buy products otherwise 'pay' button is not rendered on the page.Clicking ['pay'](https://user-images.githubusercontent.com/61980577/121951386-c6b9a680-cd52-11eb-914d-62f0a06b3f8c.png) button if transaction is successful users get redirect to ['checkout_successful'](https://user-images.githubusercontent.com/61980577/121951385-c6b9a680-cd52-11eb-81ac-1324175f8e5b.png) page which include a summary of the completed order.

* A search tab in the homepage allows users to find any product in stock, a navbar allows user to an advanced searching of products in stock which includes types of wines(white,red,rose'),champagne(blanc de blancs, blac de noirs,brut) and countries(italy,france,world).

* The account icon provides a dropdown menu including register and login link.When user is authenticated provides ['myaccount'](https://user-images.githubusercontent.com/61980577/121951384-c6b9a680-cd52-11eb-85a8-7ff2cbf35e4f.png)link leads to the users personal accounts and [logout](https://user-images.githubusercontent.com/61980577/121951383-c6211000-cd52-11eb-8652-66e37bac6a17.png) button.If user has staff status(administrator)in the dropdown menu is possible to log into a form to add new products in the stock filling all required fields(feature left to implement).

* Bag icon in the homepage top right leads to the 'cart' which provides all selected products that users have added to it.The name,sku,price,quantity and total cost of the products are displayed inside a rectangular box. It is possible to update the quantity using 'edit' button or remove the product from the cart using 'delete' button.

* The [footer](https://user-images.githubusercontent.com/61980577/121951381-c6211000-cd52-11eb-99c3-f67df5ae6377.png) provide two links: ['about'](https://user-images.githubusercontent.com/61980577/121951378-c4efe300-cd52-11eb-887f-430e97bda08c.png) that leads to a brief description of the hystory of this app and ['newsletter!](https://user-images.githubusercontent.com/61980577/121951376-c4574c80-cd52-11eb-8a2d-3cc4b062dc2c.png)'that leads to a form to fill in order to join to the app newsletter(feature left to implement)

* The text-name of the app ['worldwidewine'](https://user-images.githubusercontent.com/61980577/121952884-bacee400-cd54-11eb-8942-5e9e0bcd5cac.png) in the homepage top left is also a link which redirects users to the hompage from every pages of the site.

### The project has been validated and beautified using:

* HTML:

    • About [https://validator.w3.org/nu/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgithub.com%2FGiovanniSalvi%2FWorld_Wide_Wine%2Fblob%2Fmaster%2Fabout%2Ftemplates%2Fabout%2Fabout.html)

    • Cart [https://validator.w3.org/nu/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgithub.com%2FGiovanniSalvi%2FWorld_Wide_Wine%2Fblob%2Fmaster%2Fcart%2Ftemplates%2Fcart%2Fcart.html)

    • Checkout [https://validator.w3.org/nu/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgithub.com%2FGiovanniSalvi%2FWorld_Wide_Wine%2Fblob%2Fmaster%2Fcheckout%2Ftemplates%2Fcheckout%2Fcheckout.html)

    • Checkout_success [https://validator.w3.org/nu/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgithub.com%2FGiovanniSalvi%2FWorld_Wide_Wine%2Fblob%2Fmaster%2Fcheckout%2Ftemplates%2Fcheckout%2Fcheckout_success.html)

    • Contact [https://validator.w3.org/nu/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgithub.com%2FGiovanniSalvi%2FWorld_Wide_Wine%2Fblob%2Fmaster%2Fcontact%2Ftemplates%2Fcontact%2FcontactForm.html)

    • Index [https://validator.w3.org/nu/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgithub.com%2FGiovanniSalvi%2FWorld_Wide_Wine%2Fblob%2Fmaster%2Fhome%2Ftemplates%2Fhome%2Findex.html)

    • MyAccount [https://validator.w3.org/nu/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgithub.com%2FGiovanniSalvi%2FWorld_Wide_Wine%2Fblob%2Fmaster%2Fmyaccount%2Ftemplates%2Fmyaccount%2Fmyaccount.html)

    • AddItem [https://validator.w3.org/nu/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgithub.com%2FGiovanniSalvi%2FWorld_Wide_Wine%2Fblob%2Fmaster%2Fstock%2Ftemplates%2Fstock%2Fadd_item.html)

    • EditItem [https://validator.w3.org/nu/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgithub.com%2FGiovanniSalvi%2FWorld_Wide_Wine%2Fblob%2Fmaster%2Fstock%2Ftemplates%2Fstock%2Fedit_item.html)

    • ItemDetails [https://validator.w3.org/nu/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgithub.com%2FGiovanniSalvi%2FWorld_Wide_Wine%2Fblob%2Fmaster%2Fstock%2Ftemplates%2Fstock%2Fitem_details.html)
    
    • Stock [https://validator.w3.org/nu/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgithub.com%2FGiovanniSalvi%2FWorld_Wide_Wine%2Fblob%2Fmaster%2Fstock%2Ftemplates%2Fstock%2Fstock.html)

    • Base [https://validator.w3.org/nu/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgithub.com%2FGiovanniSalvi%2FWorld_Wide_Wine%2Fblob%2Fmaster%2Ftemplates%2Fbase.html)


* HTML: [https://webformatter.com/](https://www.freeformatter.com/html-formatter.html)

* CSS: [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fgithub.com%2FGiovanniSalvi%2FWorld_Wide_Wine%2Fblob%2Fmaster%2Fstatic%2Fcss%2Fbase.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#errors)

* CSS: [https://webformatter.com/](https://webformatter.com/)

* JAVASCRIPT: [https://jshint.com/](https://jshint.com/)

* SCRIPT.JS :<img width="1248"  src="https://user-images.githubusercontent.com/61980577/121937694-df21c500-cd42-11eb-8d63-e85f5c376157.jpg">
* STRIPE.JS :<img width="1248" src="https://user-images.githubusercontent.com/61980577/121937840-05476500-cd43-11eb-9de3-a03fa6883a2c.png">

* JAVASCRIPT: [https://webformatter.com/](https://webformatter.com/)

* PYTHON:  [http://pep8online.com/](http://pep8online.com)


### The quality of the website was measured using Google Lighthouse:

* Chrome lighthouse Tool: <img width="1272" alt="Google lighthouse" src="https://user-images.githubusercontent.com/61980577/121942775-c3212200-cd48-11eb-954b-4466b21c16b9.png">

---

### User stories :

1. As an Shopper I want

  • View a list of products to purchese
  • View price,description image to indentify the product needed.

2. As an Shopper I want 

  • Select the quantity according to my budget and avoid overspending.
  • View the price to get the best deal.

4. As an Shopper I want 

  • Search the products by name or a specific category.

5. As an Shopper I want 

  • Search the products across specific categories such(white,rose' blanc de blancs).
  
 6. As an User I want 
 
  • Quickly register for an account.
  
 7. As a User I want 
 
  • Quickly login to my personal account

  8. As a User I want 

  • Recover passwords if forget it.

  9. As a User  I want

  •  Receive a confirmation email that my regitration was successful

  10. As User I want

  • Check my personal account, update account's details and see my orsers history.
  
  
### The project has beeen designed to make pages render well on a variety of devices and window or screen sizes such as:

* Desktop: (1600x992px) Responsivness tested using ChromeDev inspector tool, as shown in the screenshot below:
<img width="1280" alt="Desktop " src="https://user-images.githubusercontent.com/61980577/121954864-24e88880-cd57-11eb-9023-a0ed4c77a4b4.png">

* Laptop: (1280x802px) Responsivness tested using ChromeDev inspector tool, as shown in the screenshot below:
<img width="778" alt="Tablet" src="https://user-images.githubusercontent.com/61980577/121954859-244ff200-cd57-11eb-852c-d8d99862e540.png">

* Tablet
 1. ipad Pro: (1024x1366px) Responsivness tested using ChromeDev inspector tool, as shown in the screenshot below:
 <img width="778" alt="iPad pro" src="https://user-images.githubusercontent.com/61980577/121954849-21550180-cd57-11eb-91bb-bd1218a0abbe.png">

 2. iPad: (768x1024px) Responsivness tested using ChromeDev inspector tool, as shown in the screenshot below:
<img width="778" alt="iPad" src="https://user-images.githubusercontent.com/61980577/121954873-274ae280-cd57-11eb-84cd-dee9f21b02e6.png">

* Mobile
 1. Moto G4 (360x640px) Responsivness tested using ChromeDev inspector tool, as shown in the screenshot below:
 <img width="778" alt="motog4" src="https://user-images.githubusercontent.com/61980577/121954871-274ae280-cd57-11eb-9b81-1f7f09b82798.png">

 2. Galaxy S5 (360x640px) Responsivness tested using ChromeDev inspector tool, as shown in the screenshot below:
 <img width="778" alt="Galaxy s5" src="https://user-images.githubusercontent.com/61980577/121954869-26b24c00-cd57-11eb-950d-a7c7ebdbfa28.png">
 
 3. Iphone 6/7/8 (375x667px) Responsivness tested using ChromeDev inspector tool, as shown in the screenshot below:
 <img width="778" alt="iPhone6:7 plus" src="https://user-images.githubusercontent.com/61980577/121954866-25811f00-cd57-11eb-8535-06fe43d21137.png">
 
 4. Iphone X (375x812px) Responsivness tested using ChromeDev inspector tool, as shown in the screenshot below:
 <img width="778" alt="iPhone x" src="https://user-images.githubusercontent.com/61980577/121954858-23b75b80-cd57-11eb-9b10-0f7ab0ba67a6.png">



---

## Deployment

### This App was deployed on Heroku server with the following steps:

* Go to [Heroku](https://id.heroku.com/login) page where you can log in or sign up for the free account than complete password and email steps.

* Once you have created an Heroku free account, click on 'Create a new app' button to create an App, then give a name to the app and select a region.


### In order to deploy the project, you need to perform some steps:

    1. 

    2. 

    3. 

    4. 

    5. 

    6. 

    7. 

    8. 

    9. 

    10. 

*   

---

# Credits


## Media

* Icons and cart Image were provided from:

    [fontawesome.com](https://fontawesome.com/v4.7.0/icons/)

### Image

* Background Images:

    [Hero Image](https://user-images.githubusercontent.com/61980577/121937363-86eac300-cd42-11eb-8efc-08e4b10b1cd8.jpeg) 

    [About Image](https://user-images.githubusercontent.com/61980577/121937365-881bf000-cd42-11eb-9b16-17cb2a365007.jpeg)

* Wines Images:
    
    [1](https://user-images.githubusercontent.com/61980577/121943216-43e01e00-cd49-11eb-9070-a5f4c74403af.jpeg)
    [2](https://user-images.githubusercontent.com/61980577/121944532-a980da00-cd4a-11eb-8470-f6387d063d84.jpeg)
    [3](https://user-images.githubusercontent.com/61980577/121944537-aab20700-cd4a-11eb-8896-178bed32eae3.jpeg)
    [4](https://user-images.githubusercontent.com/61980577/121944540-ac7bca80-cd4a-11eb-9031-11ff5077596f.jpeg)
    [5](https://user-images.githubusercontent.com/61980577/121944543-adacf780-cd4a-11eb-98e2-d6c0beefceae.jpeg)
    [6](https://user-images.githubusercontent.com/61980577/121944545-adacf780-cd4a-11eb-9094-80e607440d52.jpeg)
    [7](https://user-images.githubusercontent.com/61980577/121944550-af76bb00-cd4a-11eb-89c8-bdab7267bd4e.jpeg)
    [8](https://user-images.githubusercontent.com/61980577/121944551-b00f5180-cd4a-11eb-8d48-6469c95064a3.jpeg)
    [9](https://user-images.githubusercontent.com/61980577/121944555-b0a7e800-cd4a-11eb-9e63-d9e21aedc268.jpeg)
    [10](https://user-images.githubusercontent.com/61980577/121944562-b3a2d880-cd4a-11eb-8eaa-bc431eb8b9b3.jpeg)
    [11](https://user-images.githubusercontent.com/61980577/121944565-b3a2d880-cd4a-11eb-9772-f9d6ccd6d907.jpeg)
    [12](https://user-images.githubusercontent.com/61980577/121944569-b43b6f00-cd4a-11eb-9759-bdd3552f3d00.jpeg)
    [13](https://user-images.githubusercontent.com/61980577/121944571-b43b6f00-cd4a-11eb-9595-6969db674a45.jpeg)
    [14](https://user-images.githubusercontent.com/61980577/121944573-b4d40580-cd4a-11eb-86b2-90178fcf6dc3.jpeg)
    [15](https://user-images.githubusercontent.com/61980577/121944578-b6053280-cd4a-11eb-8ff4-e4cd340c294e.jpeg)
    [16](https://user-images.githubusercontent.com/61980577/121944579-b69dc900-cd4a-11eb-945d-72017fdc7890.jpeg)

* Cart Image:
    
    [cart](https://user-images.githubusercontent.com/61980577/121947127-991e2e80-cd4d-11eb-902a-9c5f65e55435.jpeg)
---

### Bugs 

  1. Not  bugs found.

---

### Code  

*  Javascript code for stripe payment was entirely taken from Boutique Ado then update for project's needs.

* I received inspiration for this project from: Boutique Ado

* Wines image, description and price were taken from https://www.tannico.co.uk/

* SKUs (Stock Keeping Units) are generated from https://www.tradegecko.com/free-tools/sku-generator









