Welcome! [github.com](https://github.com/GiovanniSalvi/World_Wide_Wine)

# UX

## I realized this project as part of the Full Stack Frameworks with Django module that I am attending at "code academy" training course.

### The App 

### 

### The nav menu, home-button and accounts icons  are repeated in all site's pages to get app style consistent.


---


## Project's Mockup screenshots

* [Homepage]()

* []()

* []()

* []()

* []()

* []()

* []()

---

## Features:

### Existing features

* Feature1: 

* Feature2: 

* Feature3:

* Feature4: 

* Feature5: 

* Feature6: 

* Feature7: 

* Feature8: 

* Feature9: 

### Features left to implement

* 

* 

* 

* 

* 

---

# Technology used:

## Programming languages

* HTML

* CSS

* JAVASCRIPT

* PYTHON3 + DJANGO

### Libraries

* [Bootstrap.com](https://getbootstrap.com/)

---

## Testing

### In order to navigate easily through the site:

* The homepage provides an header with the cart and account icons,a navbar to navigate through the app.The main section provides an hero image, a brief decription of the products features on sale and a link to all wines in stock.

* Clicking on 'clickhere' button in the homepage leads to the full stock of products on sale in the site(stock page).The products are displayed in three rows and are wrapped in a card container.The name ,an image, price and the country where wine is produced are displayed inside the card.

* Clicking on wine's name inside the card leads to a page containing wine's details and a brief description of the product.For site administrator is possible to update the stock deleting or editing the selected product clicking on 'delete' or 'edit' button just below wine's details.

* The two button at the bottom of products details page are 'keep shopping' button to redirect users to the stock page instead 'checkout' button leads the users to the checkout form in order to complete the orders checkout.

* Checkout page provides a form to fill in order to complete the purchase.Field required are full-name, an email address,country,city,phone number and a postal code for the delivery.Below the form, stripe payments details inputs such card number,ccv , card expiration date and a zip code are displayed.Only authenticated users are allowed to buy products otherwise 'pay' button is not rendered on the page.Clicking 'pay' button if transaction is successful users get redirect to 'checkout_successful' page which include a summary of the completed order.

* Orders details with product's name, quantity,price, total,delivery cost if included and subtotal are displayed next to checkout form in the same page.

* A search tab in the homepage allows users to find any product in stock, a navbar allows user to an advanced searching of products in stock which includes types of wines(white,red,rose'),champagne(blanc de blancs, blac de noirs,brut) and countries(italy,france,world).

* The account icon provides a dropdown menu including register and login link.When user is authenticated provides 'myaccount' link leads to the users personal accounts(feature left to implement) or logout link.If user has staff status(administrator)in the dropdown menu is possible to log into a form to add new products in the stock filling all required fields.

* Bag icon in the homepage top right leads to the 'cart' which provides all selected products that users have added to it.The name,sku,price,quantity and total cost of the products are displayed inside a rectangular box.It is possible to update the quantity using 'edit' button or remove the product from the cart using 'remove' button.

* The footer provide two links: 'about' that leads to a brief description of the hystory of this app and 'newsletter!'that leads to a form to fill in order to join to the app newsletter(feature left to implement)

* The text-name of the app 'worldwidewine' in the homepage top left is also a link which redirects users to the hompage from every pages of the site.

### The project has been validated and beautified using:

* HTML:

    • [https://validator.w3.org/nu/]()

    • [https://validator.w3.org/nu/]()

    • [https://validator.w3.org/nu/]()

    • [https://validator.w3.org/nu/]()

    • [https://validator.w3.org/nu/]()

    • [https://validator.w3.org/nu/]()

    • [https://validator.w3.org/nu/]()

    • [https://validator.w3.org/nu/]()

    • [https://validator.w3.org/nu/]()

    • [https://validator.w3.org/nu/]()
    
    • [https://validator.w3.org/nu/]()

    •  [https://validator.w3.org/nu/]()

    •  [https://validator.w3.org/nu/]()


* HTML: [https://webformatter.com/](https://validator.w3.org/)


* CSS: [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/)

* CSS: [https://webformatter.com/](https://webformatter.com/)

* JAVASCRIPT: [https://jshint.com/](https://jshint.com/)

* JAVASCRIPT:<img width="1248" alt="javascript valid" src="">


* JAVASCRIPT: [https://webformatter.com/](https://webformatter.com/)


* PYTHON: [http://pep8online.com/](http://pep8online.com/)
* PYTHON: <img width="1440" alt="python code Validation" src="">


### The quality of the website was measured using Google Lighthouse:

* Chrome lighthouse Tool: <img width="1272" alt="Google lighthouse" src="">

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
<img width="1280" alt="Desktop " src="">

* Laptop: (1280x802px) Responsivness tested using ChromeDev inspector tool, as shown in the screenshot below:
<img width="778" alt="Tablet" src="">

* Tablet
 1. ipad Pro: (1024x1366px) Responsivness tested using ChromeDev inspector tool, as shown in the screenshot below:
 <img width="778" alt="iPad pro" src="">

 2. iPad: (768x1024px) Responsivness tested using ChromeDev inspector tool, as shown in the screenshot below:
<img width="778" alt="iPad" src="">

* Mobile
 1. Moto G4 (360x640px) Responsivness tested using ChromeDev inspector tool, as shown in the screenshot below:
 <img width="778" alt="motog4" src="">

 2. Galaxy S5 (360x640px) Responsivness tested using ChromeDev inspector tool, as shown in the screenshot below:
 <img width="778" alt="Galaxy s5" src="">
 
 3. Iphone 6/7/8 Plus (414x736px) Responsivness tested using ChromeDev inspector tool, as shown in the screenshot below:
 <img width="778" alt="iPhone6:7 plus" src="">

 4. Iphone 6/7/8 (375x667px) Responsivness tested using ChromeDev inspector tool, as shown in the screenshot below:
 <img width="778" alt="iPhone 6:7" src="">
 
 5. Iphone X (375x812px) Responsivness tested using ChromeDev inspector tool, as shown in the screenshot below:
 <img width="778" alt="iPhone x" src="">



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

* Social-media icons were provided from:

    [fontawesome.com](https://fontawesome.com/v4.7.0/icons/)


### Image

* Hero Image provide from:

    [Hero Image]()

    [Hero Image]()

---

### Bugs 

  1. Not significant bugs found.

---

### Code  

* 









