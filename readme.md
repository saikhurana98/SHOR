# SastiCopy : Concept store

A store for all the saste ka maal.

## Understanding the concept of the store

Caters to the mass market, however by limiting the number of products in the
inventory at any given point of time, helps move product,
improves the unit economics, as well as
creates a degree of exclusivity.

Products are only available for up to 10 days, therefore invoking a sense of
urgency in the customer's buying pattern. Combined with low prices, this
is the perfect combination for impulse buying.

## Hard requirements imposed by project description on classroom
- Search Functionality(DONE)
  - Check if the redirects work
- Wishlist Functionality()
- User profile display page
- Review page for a given product
- My orders page

## Abstract Requirements for such a store

- Great User Design : Bring a premium feel to the product
- Simple Process Flow : No sophisticated/ remarkably complex user flows.
- Ready to deploy : Should be ready for deployment.
- Basic Security :  Security from the more common attacks.

## Hard requirements for a store

- Authentication mechanism
- Landing page crafted with best practice design principles.
- Showcase of different category Products
- Product timer : 10 days individually.
- Cart : Adding items for buying, and then storing inside the cookies.
- Checkout mechanism : Page that totalls the amount of everything inside the cart, then redirects to payment gateway.
- Tracking : Generates tracking number for each parcel, can be tracked with third-party delivery partner. Eg : Bluedart
- Blog : Showcasing the products when they're launched

## Important features already implemented ( Keep updating )
- Authentication mechanism.
- Landing page
- Product static page
- Checkout static page
- Tracking static pages
- Blog static pages


## Important on the to-do list ( Keep updating )
- (resolved)Database schema change around to handle images, product details, timer.
- (resolved)Database schema add for blog posts. --> Scratch this - Better idea just keep it static because users aren't changing this
- (resolved)Database schema add tracking ability
- (resolved)Blog posts --> Ask 2 people to write in html with frontend and all.
- (resolved)Showcase (Update with the help of filters? --> Use AJAX) // Use different pages to display different products
- (removed)Search Functionality
- (resolved)Cart implementation in database : for every user
- Checkout page - Make dynamic
- Tracking page

## Changes made since last commit
- Backend written for the cart.
- User just includes reciept and tracking now.
- Checkout and cart have been migrated to the shop
- Index does the database query and passes to the template.

## Issues
- (Resolved) Product table isn't getting appropriately initialised
- (Resolved) Checkout page doesn't work
- (Not Resolved) Frontend needs to render the product details being passed to it in Shop-> Category Page.
- (Not Resolved) Test that the product renderings work for individual product displays.
- (Not Resolved) Incomplete Cart
