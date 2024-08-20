### Context

On Airbnb, anyone who has a room or a property of any kind (apartment, house, chalet, inn, etc.) can offer it for rent on daily rental.

You create your host profile (a person who offers a property for daily rental) and then create a listing for your property.

In this listing, the host should describe the property's features as thoroughly as possible to help renters/travelers choose the best property for them (and to make your listing more attractive).

There are dozens of customization options for your listing, ranging from minimum stay duration, price, and number of rooms to cancellation policies, extra guest fees, identity verification requirements for the renter, and more.

### Our objective

Build a price prediction model that allows an ordinary person with a property to know how much they should charge for the daily rental of their property.

Alternatively, for the average renter, given the property they are looking for, the model can help determine whether the property is priced attractively (below the average for properties with similar characteristics) or not.

### What we have available, inspirations, and credits.

The datasets were taken from the Kaggle website: https://www.kaggle.com/allanbruno/airbnb-rio-de-janeiro.

If you want an alternative solution, we can look at the solution from Kaggle user Allan Bruno in the Notebook: https://www.kaggle.com/allanbruno/helping-regular-people-price-listings-on-airbnb.

- The datasets consist of property prices and their respective characteristics for each month.
- Prices are given in Brazilian Reais (R$).
- We have datasets from April 2018 to May 2020, except for June 2018, which does not have a dataset.

### Initial Expectations

- I believe seasonality could be an important factor, as months like December and January (Summer + Holidays + School Vacation) tend to be quite expensive in Rio de Janeiro.
- The property's location should make a big difference in price, since in Rio de Janeiro, the location can completely change the characteristics of the area (safety, natural beauty, tourist attractions).
- Extras/Amenities might have a significant impact, given that there are many old buildings and houses in Rio de Janeiro.

Let's find out how much these factors influence the price and whether there are other less intuitive factors that are extremely important.
