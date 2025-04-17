
{% extends 'Website/layout2.html' %}
{% load static %}
{% load user_tags %}

{% block body %}
<div class="wrapper ovh">

    {% include 'Website/top_header.html' %}
    {% include 'Website/top_navbar.html' %}


    <!-- Modal -->
    {% include 'Website/login_modal.html' %}
    {% include 'Website/dealer_form.html' %}

    <!-- Home Design -->
    <section class="home-one mt0 mt70-992 p0">
        <div class="container-fluid p0">
            <div class="row desktop-banner">
                <div class="col-lg-12">
                    <div class="main-banner-wrapper home3_style">
                        <div class="banner-style-one no-dots owl-theme owl-carousel">
                            <div class="slide slide-one"
                                style="background-image: url({% static 'images/dcb-sell-car-banner.webp' %});height: 640px;">
                                <div class="container">
                                    <div class="row home-content pl20">

                                    </div>
                                </div>
                            </div>
                            <div class="slide slide-one"
                                style="background-image: url({% static 'images/dcb-images/dream-car-bazaar-banner.webp' %});height: 640px;">
                                <div class="container">
                                    <div class="row home-content pl20">

                                    </div>
                                </div>
                            </div>
                            
                            <div class="slide slide-one"
                                style="background-image: url({% static 'images/dcb-images/dream-car-bazaar-banner-2.webp' %});height: 640px;">
                                <div class="container">
                                    <div class="row home-content pl20">

                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="carousel-btn-block banner-carousel-btn">
                            <span class="carousel-btn left-btn"><i class="flaticon-left-arrow left"></i></span>
                            <span class="carousel-btn right-btn"><i class="flaticon-right-arrow right"></i></span>
                        </div>
                        <!-- /.carousel-btn-block banner-carousel-btn -->
                    </div>
                    <!-- /.main-banner-wrapper -->
                </div>
            </div>
            <div class="row mobile-view">
                <div class="col-lg-12">
                    <div class="main-banner-wrapper home3_style">
                        <div class="banner-style-one no-dots owl-theme owl-carousel">
                            <div class="slide slide-one"
                                style="background-image: url({% static 'images/dcb-mobile-sell-car-banner.webp' %});height: 640px;">
                                <div class="container">
                                    <div class="row home-content pl20">

                                    </div>
                                </div>
                            </div>
                            <div class="slide slide-one"
                                style="background-image: url({% static 'images/dcb-images/mobile-dream-car-bazaar-banner.webp' %});height: 640px;">
                                <div class="container">
                                    <div class="row home-content pl20">

                                    </div>
                                </div>
                            </div>
                            
                            <div class="slide slide-one"
                                style="background-image: url({% static 'images/dcb-images/mobile-dream-car-bazaar-banner-2.webp' %});height: 640px;">
                                <div class="container">
                                    <div class="row home-content pl20">

                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="carousel-btn-block banner-carousel-btn">
                            <span class="carousel-btn left-btn"><i class="flaticon-left-arrow left"></i></span>
                            <span class="carousel-btn right-btn"><i class="flaticon-right-arrow right"></i></span>
                        </div>
                        <!-- /.carousel-btn-block banner-carousel-btn -->
                    </div>
                    <!-- /.main-banner-wrapper -->
                </div>
            </div>
        </div>
    </section>
    <!--====================================================End Section=================================-->

    <!-- Extra Features -->
    <section class="features pt50 pb50 bgc-thm2">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="home1_advance_search_wrapper home3_style">
                        <form method="get" action="{% url 'website_car_filter' %}">
                            <ul class="mb0 text-center d-block">
                                <div class="row">
                                    <div class="col-lg-3 col-sm-12"><li>
                                    <div class="select-boxes">
                                        <div class="car_models">
                                            <select class="form-select" name="car_brand" id="car_brand">
                                                <option>Select Brands</option>
                                                {% for car_brand in car_brands %}
                                                    <option value="{{car_brand.id}}">{{car_brand.name}}</option>
                                                {% endfor %}
                                            </select>
                                        </div>
                                    </div>
                                </li>
                                </div>
                                    <div class="col-lg-3 col-sm-12">
                                        <li>
                                    <div class="select-boxes">
                                        <div class="car_models" id="car_models">
                                            <select class="form-select" id="car_model" name="car_model">
                                                <option value="">---------</option>
                                            </select>
                                        </div>
                                    </div>
                                </li>
                                    </div>
                                    <div class="col-lg-3 col-sm-12">
                                        <li>
                                    <div class="select-boxes">
                                        <div class="car_prices">
                                            <select class="form-select" id="car_variants" name="car_variants">
                                                <option value="">---------</option>
                                            
                                            </select>
                                        </div>
                                    </div>
                                </li>
                                    </div>
                                    <div class="col-lg-3 col-sm-12">
                                        <li>
                                    <div class="d-block">
                                        <button type="submit" class="btn btn-thm advnc_search_form_btn"><span
                                                class="flaticon-magnifiying-glass"></span>Search</button>
                                    </div>
                                </li>
                                    </div>
                                </div>
                            </ul>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Buy or Sell Car -->
    <section class="pt60 bb1">
        <div class="container">
            <div class="row">
                <div class="col-md-6 wow fadeInLeft" data-wow-duration="1s" data-wow-delay="0.1s">
                    <div class="iconbox_home2 home6_style d-block d-lg-flex mb30-sm text-center text-md-start">
                        <div class="icon me-2 wobble-horizontal"><span class="flaticon-car-1"></span></div>
                        <div class="details ms-0 ms-lg-4">
                            <a href="#">
                                <h3 class="title">Are You looking for Buy a car?</h3>
                            </a>
                            <p>Search your car in our Inventory and request a quote on the vehicle of your choosing.
                            </p>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 wow fadeInRight" data-wow-duration="1s" data-wow-delay="0.3s">
                    <div class="iconbox_home2 home6_style style2 text-center text-md-end">
                        <div class="icon float-none float-lg-end ms-0 ms-lg-4 wobble-horizontal"><span
                                class="flaticon-car-2"></span></div>
                        <div class="details">
                            <a href="#">
                                <h3 class="title">Are You looking for Sell a car?</h3>
                            </a>
                            <p>Request search your car in our Inventory and a quote on the vehicle of your choosing.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- End Section -->

    <!-- Car Category -->
    <section class="car-category mobile_space bgc-f9 z-2 pb70" style="background: #eeeeee;">
        <div class="container">
            <div class="row">
                <div class="col-6 col-sm-6 col-md-4 col-lg col-xl wow fadeInUp" data-wow-duration="1s"
                    data-wow-delay="0.1s" style="visibility: visible; animation-duration: 1s; animation-delay: 0.1s;">
                    <div class="category_item">
                        <div class="thumb">
                            <img src="{% static 'images/category-item/1.png' %}" alt="1.png">
                        </div>
                        <div class="details">
                            <p class="title"><a href="#">Compact</a></p>
                        </div>
                    </div>
                </div>
                <div class="col-6 col-sm-6 col-md-4 col-lg col-xl wow fadeInUp" data-wow-duration="1s"
                    data-wow-delay="0.3s" style="visibility: visible; animation-duration: 1s; animation-delay: 0.3s;">
                    <div class="category_item">
                        <div class="thumb">
                            <img src="{% static 'images/category-item/2.png' %}" alt="2.png">
                        </div>
                        <div class="details">
                            <p class="title"><a href="#">Sedan</a></p>
                        </div>
                    </div>
                </div>
                <div class="col-6 col-sm-6 col-md-4 col-lg col-xl wow fadeInUp" data-wow-duration="1s"
                    data-wow-delay="0.5s" style="visibility: visible; animation-duration: 1s; animation-delay: 0.5s;">
                    <div class="category_item">
                        <div class="thumb">
                            <img src="{% static 'images/category-item/3.png' %}" alt="3.png">
                        </div>
                        <div class="details">
                            <p class="title"><a href="#">SUV</a></p>
                        </div>
                    </div>
                </div>
                <div class="col-6 col-sm-6 col-md-4 col-lg col-xl wow fadeInUp" data-wow-duration="1s"
                    data-wow-delay="0.7s" style="visibility: visible; animation-duration: 1s; animation-delay: 0.7s;">
                    <div class="category_item">
                        <div class="thumb">
                            <img src="{% static 'images/category-item/4.png' %}" alt="4.png">
                        </div>
                        <div class="details">
                            <p class="title"><a href="#">Convertible</a></p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4 col-lg col-xl wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.9s"
                    style="visibility: visible; animation-duration: 1s; animation-delay: 0.9s;">
                    <div class="category_item">
                        <div class="thumb">
                            <img src="{% static 'images/category-item/5.png' %}" alt="5.png">
                        </div>
                        <div class="details">
                            <p class="title"><a href="#">Coupe</a></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- End Section -->

    <!-- Featured Car Section -->
    <section class="whychose_us">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <div class="main-title text-center">
                        <h2>Featured Cars Special Offers</h2>
                    </div>
                </div>
            </div>
            <div class="featured-car-row">
                <div class="row">
                    <div class="col-list-3 col-list-12">
                        <div class="featured-car-list">
                            <div class="featured-car-img">
                                <a href=""><img src="{% static 'images/images/featured-img-01.jpg' %}" class="img-fluid"
                                        alt="Image"></a>
                                <div class="label_icon">Trending</div>
                            </div>
                            <div class="featured-car-content">
                                <h6><a href="#">Maserati QUATTROPORTE 1,6</a></h6>
                                <div class="price_info">
                                    <p class="featured-price">Rs90,000</p>
                                    <div class="car-location"><span><i class="fa fa-map-marker" aria-hidden="true"></i>
                                            Colorado, USA</span></div>
                                </div>
                                <ul>
                                    <li><i class="fa fa-road" aria-hidden="true"></i>0,000 km</li>
                                    <li><i class="fa fa-tachometer" aria-hidden="true"></i>30.000 miles</li>
                                    <li><i class="fa fa-calendar" aria-hidden="true"></i>2005 model</li>
                                    <li><i class="fa fa-car" aria-hidden="true"></i>Diesel</li>
                                    <li><i class="fa fa-user" aria-hidden="true"></i>5 seats</li>
                                    <li><i class="fa fa-superpowers" aria-hidden="true"></i>143 kW</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div class="col-list-3 col-list-12">
                        <div class="featured-car-list">
                            <div class="featured-car-img">
                                <a href=""><img src="{% static 'images/images/featured-img-02.jpg' %}" class="img-fluid"
                                        alt="Image"></a>
                                <div class="label_icon">Trending</div>
                            </div>
                            <div class="featured-car-content">
                                <h6><a href="#">Mazda CX-5 SX, V6, ABS, Sunroof</a></h6>
                                <div class="price_info">
                                    <p class="featured-price">Rs90,000</p>
                                    <div class="car-location"><span><i class="fa fa-map-marker" aria-hidden="true"></i>
                                            Colorado, USA</span></div>
                                </div>
                                <ul>
                                    <li><i class="fa fa-road" aria-hidden="true"></i>0,000 km</li>
                                    <li><i class="fa fa-tachometer" aria-hidden="true"></i>30.000 miles</li>
                                    <li><i class="fa fa-calendar" aria-hidden="true"></i>2005 model</li>
                                    <li><i class="fa fa-car" aria-hidden="true"></i>Diesel</li>
                                    <li><i class="fa fa-user" aria-hidden="true"></i>5 seats</li>
                                    <li><i class="fa fa-superpowers" aria-hidden="true"></i>143 kW</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div class="col-list-3 col-list-12">
                        <div class="featured-car-list">
                            <div class="featured-car-img">
                                <a href=""><img src="{% static 'images/images/featured-img-03.jpg' %}" class="img-fluid"
                                        alt="Image"></a>
                                <div class="label_icon">Trending</div>
                            </div>
                            <div class="featured-car-content">
                                <h6><a href="#">BMW 535i</a></h6>
                                <div class="price_info">
                                    <p class="featured-price">Rs90,000</p>
                                    <div class="car-location"><span><i class="fa fa-map-marker" aria-hidden="true"></i>
                                            Colorado, USA</span></div>
                                </div>
                                <ul>
                                    <li><i class="fa fa-road" aria-hidden="true"></i>0,000 km</li>
                                    <li><i class="fa fa-tachometer" aria-hidden="true"></i>30.000 miles</li>
                                    <li><i class="fa fa-calendar" aria-hidden="true"></i>2005 model</li>
                                    <li><i class="fa fa-car" aria-hidden="true"></i>Diesel</li>
                                    <li><i class="fa fa-user" aria-hidden="true"></i>5 seats</li>
                                    <li><i class="fa fa-superpowers" aria-hidden="true"></i>143 kW</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- End Section -->

    <!-- Our Popular Listing -->
    {% include 'Website/feature_car_list.html' %}
    <!-- End Section -->

    <!-- DreamCarBazaar Services Section -->
    <section class="whychose_us" style="background: #f2f2f2;">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <div class="main-title text-center">
                        <h2>DreamCarBazaar Services</h2>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-3 col-md-6 col-sm-12">
                    <div class="dcb-service-card">
                        <div class="img-con">
                            <img height="135" width="180" src="{% static 'images/dcb-images/sell-you-car.png' %}"
                                alt="Services 3">
                        </div>
                        <div class="text-part">
                            <div>
                                <h5 class="mb20 mt20 dcb-card-title">Sell Your Car</h5>
                                <p class="color-gray m8t m8b font14">Sell your pre-owned car at the best value with
                                    Dream CarBazaar. Get the best price for your vehicle.
                                </p>
                            </div>
                            <div class="explore-more-btn">Explore More <i class="fa fa-arrow-right"></i> </div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6 col-sm-12">
                    <div class="dcb-service-card">
                        <div class="img-con">
                            <img height="135" width="180" src="{% static 'images/dcb-images/sell-you-car.png' %}"
                                alt="Services 3">
                        </div>
                        <div class="text-part">
                            <div>
                                <h5 class="mb20 mt20 dcb-card-title">Buy A Car</h5>
                                <p class="color-gray m8t m8b font14">Choose your dream car from a wide range of
                                    pre-owned vehicles and get the best deal from our experts.
                                </p>
                            </div>
                            <div class="explore-more-btn">Explore More <i class="fa fa-arrow-right"></i> </div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6 col-sm-12">
                    <div class="dcb-service-card">
                        <div class="img-con">
                            <img height="135" width="180" src="{% static 'images/dcb-images/car-insurance.png' %}"
                                alt="Services 3">
                        </div>
                        <div class="text-part">
                            <div>
                                <h5 class="mb20 mt20 dcb-card-title">Car Insurance</h5>
                                <p class="color-gray m8t m8b font14">We make sure that your car is fully safe and
                                    protected against any damage or accident. Secure your vehicle with our full
                                    insurance services.
                                </p>
                            </div>
                            <div class="explore-more-btn">Explore More <i class="fa fa-arrow-right"></i> </div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6 col-sm-12">
                    <div class="dcb-service-card">
                        <div class="img-con">
                            <img height="135" width="180" src="{% static 'images/dcb-images/car-lone.png' %}"
                                alt="Services 3">
                        </div>
                        <div class="text-part">
                            <div>
                                <h5 class="mb20 mt20 dcb-card-title">Car Loan</h5>
                                <p class="color-gray m8t m8b font14">Apply for a loan and take your vehicle home with
                                    easy loan assistance. Easy to apply and get attractive ROI.
                                </p>
                            </div>
                            <div class="explore-more-btn">Explore More <i class="fa fa-arrow-right"></i> </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- End Section -->

    <!-- Sell Your Car -->
    <section class="pt50 pb50 sell-car-cta">
        <div class="container">
            <div class="row">
                <div class="col-lg-7 col-sm-12 mt20">
                    <div>
                        <h2>Sell 100% online in very simple steps</h2>
                        <h3>Enter a few details, get our best offer, and leave pickup to us.</h3>
                        <button>Sell Your Car</button>
                    </div>
                </div>
                <div class="col-lg-5 col-sm-12">
                    <div>
                        <img src="{% static 'images/dcb-images/sell-your-car.png' %}" alt="">
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- End Section -->

    <!-- Popular Brands -->
    <section class="our-team pb80 pt80">
        <div class="container">
            <div class="row">
                <div class="col-lg-6 offset-lg-3">
                    <div class="main-title text-center">
                        <h2>Popular Brands</h2>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-12">
                    <div class="team_slider">
                        <div class="listing_item_6grid_slider dots_none">
                            <div class="item">
                                <div class="team_member popular-brand">
                                    <div class="thumb"> <img class="img-fluid popular-brands" width="100"
                                            src="{% static 'images/images/ford.webp' %}" alt="1.jpg"></div>
                                </div>
                            </div>
                            <div class="item">
                                <div class="team_member popular-brand">
                                    <div class="thumb"> <img class="img-fluid popular-brands" width="100"
                                            src="{% static 'images/images/audi.webp' %}" alt="2.jpg"></div>
                                </div>
                            </div>
                            <div class="item">
                                <div class="team_member popular-brand">
                                    <div class="thumb"> <img class="img-fluid popular-brands" width="100"
                                            src="{% static 'images/images/honda.webp' %}" alt="3.jpg"></div>
                                </div>
                            </div>
                            <div class="item">
                                <div class="team_member popular-brand">
                                    <div class="thumb"> <img class="img-fluid popular-brands" width="100"
                                            src="{% static 'images/images/hyundai.webp' %}" alt="4.jpg"></div>
                                </div>
                            </div>
                            <div class="item">
                                <div class="team_member popular-brand">
                                    <div class="thumb"> <img class="img-fluid popular-brands" width="100"
                                            src="{% static 'images/images/jeep.webp' %}" alt="1.jpg"></div>
                                </div>
                            </div>
                            <div class="item">
                                <div class="team_member popular-brand">
                                    <div class="thumb"> <img class="img-fluid popular-brands" width="100"
                                            src="{% static 'images/images/kia.webp' %}" alt="2.jpg"></div>
                                </div>
                            </div>
                            <div class="item">
                                <div class="team_member popular-brand">
                                    <div class="thumb"> <img class="img-fluid popular-brands" width="100"
                                            src="{% static 'images/images/mahindra.webp' %}" alt="3.jpg"></div>
                                </div>
                            </div>
                            <div class="item">
                                <div class="team_member popular-brand">
                                    <div class="thumb"> <img class="img-fluid popular-brands" width="100"
                                            src="{% static 'images/images/maruti.webp' %}" alt="4.jpg"></div>
                                </div>
                            </div>
                            <div class="item">
                                <div class="team_member popular-brand">
                                    <div class="thumb"> <img class="img-fluid popular-brands" width="100"
                                            src="{% static 'images/images/mercedes-benz.webp' %}" alt="1.jpg"></div>
                                </div>
                            </div>
                            <div class="item">
                                <div class="team_member popular-brand">
                                    <div class="thumb"> <img class="img-fluid popular-brands" width="100"
                                            src="{% static 'images/images/mg.webp' %}" alt="2.jpg"></div>
                                </div>
                            </div>
                            <div class="item">
                                <div class="team_member popular-brand">
                                    <div class="thumb"> <img class="img-fluid popular-brands" width="100"
                                            src="{% static 'images/images/nissan.webp' %}" alt="3.jpg"></div>
                                </div>
                            </div>
                            <div class="item">
                                <div class="team_member popular-brand">
                                    <div class="thumb"> <img class="img-fluid popular-brands" width="100"
                                            src="{% static 'images/images/renault.webp' %}" alt="4.jpg"></div>
                                </div>
                            </div>
                            <div class="item">
                                <div class="team_member popular-brand">
                                    <div class="thumb"> <img class="img-fluid popular-brands" width="100"
                                            src="{% static 'images/images/skoda.webp' %}" alt="1.jpg"></div>
                                </div>
                            </div>
                            <div class="item">
                                <div class="team_member popular-brand">
                                    <div class="thumb"> <img class="img-fluid popular-brands" width="100"
                                            src="{% static 'images/images/tata.webp' %}" alt="2.jpg"></div>
                                </div>
                            </div>
                            <div class="item">
                                <div class="team_member popular-brand">
                                    <div class="thumb"> <img class="img-fluid popular-brands" width="100"
                                            src="{% static 'images/images/toyota.webp' %}" alt="3.jpg"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- End Section -->

    <!-- We are best section-->
    <section class="we-are-best"
        style="background: url({% static 'images/cars-bg.jpg' %});background-size:cover;background-position: center;background-attachment: fixed;">
        <div class="bg-overlay"></div>
        <div class="container">
            <div class="row">
                <div class="col-lg-6 m-auto">
                    <div class="main-title text-center text-light">
                        <h2 class="text-white">We Are The Best</h2>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-sm-6 col-xl-3 wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.1s"
                    style="visibility: visible; animation-duration: 1s; animation-delay: 0.1s;">
                    <div class="iconbox_home4_style mb30-lg">
                        <div class="icon one"><span class="flaticon-user-1"></span></div>
                        <div class="details">
                            <h4 class="title">Carefully Inspected</h4>
                            <p>All our cars are carefully inspected before buying and selling through our quality
                                inspection.</p>
                        </div>
                    </div>
                </div>
                <div class="col-sm-6 col-xl-3 wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.3s"
                    style="visibility: visible; animation-duration: 1s; animation-delay: 0.3s;">
                    <div class="iconbox_home4_style mb30-lg mt60 mt0-lg">
                        <div class="icon two"><span class="flaticon-high-five"></span></div>
                        <div class="details">
                            <h4 class="title">Assured Benefits</h4>
                            <p>Avail exciting benefits with us on purchasing your vehicle. Get a 1-year warranty with us
                                on your purchase.</p>
                        </div>
                    </div>
                </div>
                <div class="col-sm-6 col-xl-3 wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.5s"
                    style="visibility: visible; animation-duration: 1s; animation-delay: 0.5s;">
                    <div class="iconbox_home4_style mb30-lg">
                        <div class="icon three"><span class="flaticon-megaphone"></span></div>
                        <div class="details">
                            <h4 class="title">Trusted Agents</h4>
                            <p>Our stress-free finance department is always there to find you financial solutions to
                                save your money. </p>
                        </div>
                    </div>
                </div>
                <div class="col-sm-6 col-xl-3 wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.7s"
                    style="visibility: visible; animation-duration: 1s; animation-delay: 0.7s;">
                    <div class="iconbox_home4_style mb30-lg mt60 mt0-lg">
                        <div class="icon four"><span class="flaticon-headphones"></span></div>
                        <div class="details">
                            <h4 class="title">Free Support</h4>
                            <p>Connect with us whenever you want while selling or buying your vehicle. Get 24-hour
                                support for any enquiries.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- End Section -->

    <!-- Our Plans -->
    <section class="inventory-section pt-100 pb-70">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <div class="main-title text-center">
                        <h2>Our Plans</h2>
                    </div>
                </div>
            </div>
            <div class="row align-items-center">
                <div class="col-md-6 col-lg-4">
                    <div class="single-inventory">
                        <div class="inventory-top">
                            <h3>Silver Package</h3>
                            <h4>Rs<span>88.99</span>/per month</h4>
                            <div class="image">
                                <img src="{% static 'images/images/1.png' %}" alt="Image">
                            </div>
                            <div class="hover-image">
                                <img src="{% static 'images/images/2.png' %}" alt="Image">
                            </div>
                        </div>
                        <div class="inventroy-content">
                            <ul>
                                <li>
                                    <i class="fa fa-check"></i> Departure of a specialist
                                </li>
                                <li>
                                    <i class="fa fa-check"></i> Inspection report
                                </li>
                                <li>
                                    <i class="fa fa-check"></i> Body Inspection
                                </li>
                            </ul>
                            <a href="#" class="custom-btn2">Get Plan</a>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 col-lg-4">
                    <div class="single-inventory active-color">
                        <div class="inventory-top">
                            <h3>Platinum Package</h3>
                            <h4>Rs<span>288.99</span>/per month</h4>
                            <div class="hover-image">
                                <img src="{% static 'images/images/1.png' %}" alt="Image">
                            </div>
                            <div class="image">
                                <img src="{% static 'images/images/2.png' %}" alt="Image">
                            </div>
                        </div>
                        <div class="inventroy-content">
                            <ul>
                                <li>
                                    <i class="fa fa-check"></i> Departure of a specialist
                                </li>
                                <li>
                                    <i class="fa fa-check"></i> Inspection report
                                </li>
                                <li>
                                    <i class="fa fa-check"></i> Body Inspection
                                </li>
                                <li>
                                    <i class="fa fa-check"></i> Computer Diagnostic
                                </li>
                                <li>
                                    <i class="fa fa-check"></i> Inspection of saloon
                                </li>
                                <li>
                                    <i class="fa fa-check"></i> Electricians
                                </li>
                            </ul>
                            <a href="#" class="custom-btn2">Get Plan</a>
                        </div>
                    </div>
                </div>
                <div class="offset-md-3 offset-lg-0 col-md-6 col-lg-4">
                    <div class="single-inventory">
                        <div class="inventory-top">
                            <h3>Silver Package</h3>
                            <h4>Rs<span>88.99</span>/per month</h4>
                            <div class="image">
                                <img src="{% static 'images/images/1.png' %}" alt="Image">
                            </div>
                            <div class="hover-image">
                                <img src="{% static 'images/images/2.png' %}" alt="Image">
                            </div>
                        </div>
                        <div class="inventroy-content">
                            <ul>
                                <li>
                                    <i class="fa fa-check"></i> Departure of a specialist
                                </li>
                                <li>
                                    <i class="fa fa-check"></i> Inspection report
                                </li>
                                <li>
                                    <i class="fa fa-check"></i> Body Inspection
                                </li>
                            </ul>
                            <a href="#" class="custom-btn2">Get Plan</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- End Section -->

    <!-- Our Popular Listing -->
    <section class="popular-listing">
        <div class="container">
            <div class="row">
                <div class="col-lg-6 offset-lg-3">
                    <div class="main-title text-center">
                        <h2>Browse By Type</h2>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6 wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.1s">
                    <div class="explore_city home6_style">
                        <div class="thumb">
                            <div class="listing_footer">
                                <ul class="mb0">
                                    <li class="list-inline-item"><a href="#"><span
                                                class="flaticon-road-perspective me-2"></span>77362</a></li>
                                    <li class="list-inline-item"><a href="#"><span
                                                class="flaticon-gas-station me-2"></span>Diesel</a></li>
                                    <li class="list-inline-item"><a href="#"><span
                                                class="flaticon-gear me-2"></span>Automatic</a></li>
                                </ul>
                            </div>
                            <img class="img-fluid" src="{% static 'images/listing/browse1.jpg' %}" alt="browse1.jpg">
                        </div>
                        <div class="details">
                            <h4 class="title"><a href="#">Compact</a></h4>
                            <p>0 Listings</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.3s">
                    <div class="explore_city home6_style">
                        <div class="thumb">
                            <div class="listing_footer">
                                <ul class="mb0">
                                    <li class="list-inline-item"><a href="#"><span
                                                class="flaticon-road-perspective me-2"></span>77362</a></li>
                                    <li class="list-inline-item"><a href="#"><span
                                                class="flaticon-gas-station me-2"></span>Diesel</a></li>
                                    <li class="list-inline-item"><a href="#"><span
                                                class="flaticon-gear me-2"></span>Automatic</a></li>
                                </ul>
                            </div>
                            <img class="img-fluid" src="{% static 'images/listing/browse2.jpg' %}" alt="browse2.jpg">
                        </div>
                        <div class="details">
                            <h4 class="title"><a href="#">Sedan</a></h4>
                            <p>0 Listings</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 col-lg-4 wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.5s">
                    <div class="explore_city home6_style">
                        <div class="thumb">
                            <div class="listing_footer">
                                <ul class="mb0">
                                    <li class="list-inline-item"><a href="#"><span
                                                class="flaticon-road-perspective me-2"></span>77362</a></li>
                                    <li class="list-inline-item"><a href="#"><span
                                                class="flaticon-gas-station me-2"></span>Diesel</a></li>
                                    <li class="list-inline-item"><a href="#"><span
                                                class="flaticon-gear me-2"></span>Automatic</a></li>
                                </ul>
                            </div>
                            <img class="img-fluid" src="{% static 'images/listing/browse3.jpg' %}" alt="browse3.jpg">
                        </div>
                        <div class="details">
                            <h4 class="title"><a href="#">SUV</a></h4>
                            <p>0 Listings</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 col-lg-4 wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.7s">
                    <div class="explore_city home6_style">
                        <div class="thumb">
                            <div class="listing_footer">
                                <ul class="mb0">
                                    <li class="list-inline-item"><a href="#"><span
                                                class="flaticon-road-perspective me-2"></span>77362</a></li>
                                    <li class="list-inline-item"><a href="#"><span
                                                class="flaticon-gas-station me-2"></span>Diesel</a></li>
                                    <li class="list-inline-item"><a href="#"><span
                                                class="flaticon-gear me-2"></span>Automatic</a></li>
                                </ul>
                            </div>
                            <img class="img-fluid" src="{% static 'images/listing/browse4.jpg' %}" alt="browse4.jpg">
                        </div>
                        <div class="details">
                            <h4 class="title"><a href="#">Convertible</a></h4>
                            <p>0 Listings</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-6 col-lg-4 wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.9s">
                    <div class="explore_city home6_style">
                        <div class="thumb">
                            <div class="listing_footer">
                                <ul class="mb0">
                                    <li class="list-inline-item"><a href="#"><span
                                                class="flaticon-road-perspective me-2"></span>77362</a></li>
                                    <li class="list-inline-item"><a href="#"><span
                                                class="flaticon-gas-station me-2"></span>Diesel</a></li>
                                    <li class="list-inline-item"><a href="#"><span
                                                class="flaticon-gear me-2"></span>Automatic</a></li>
                                </ul>
                            </div>
                            <img class="img-fluid" src="{% static 'images/listing/browse5.jpg' %}" alt="browse5.jpg">
                        </div>
                        <div class="details">
                            <h4 class="title"><a href="#">Coupe</a></h4>
                            <p>0 Listings</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- End Section -->

    <!-- How It Works -->
    <section class="whychose_us">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <div class="main-title text-center">
                        <h2>Why Choose Us?</h2>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-6">
                    <div class="row">
                        <div class="col-sm-6 wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.1s">
                            <div class="iconbox_home6_style">
                                <div class="icon one"><span class="flaticon-user-1"></span></div>
                                <div class="details">
                                    <h4 class="title">One-Stop Solution</h4>
                                    <p>Here you will get all the solutions whether you want to buy a car, sell it, or
                                        get a car loan and insurance.</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-sm-6 wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.3s">
                            <div class="iconbox_home6_style">
                                <div class="icon two"><span class="flaticon-high-five"></span></div>
                                <div class="details">
                                    <h4 class="title">Best Value</h4>
                                    <p>Whether you are the buyer or the seller you will get the best value for the
                                        vehicle. Get the best value for your old car.</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-sm-6 wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.5s">
                            <div class="iconbox_home6_style">
                                <div class="icon three"><span class="flaticon-megaphone"></span></div>
                                <div class="details">
                                    <h4 class="title">Sell Online</h4>
                                    <p>Sell your vehicle online through our website from the comfort of your home. Easy
                                        and transparent process.</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-sm-6 wow fadeInUp" data-wow-duration="1s" data-wow-delay="0.7s">
                            <div class="iconbox_home6_style">
                                <div class="icon four"><span class="flaticon-headphones"></span></div>
                                <div class="details">
                                    <h4 class="title">Vehicle Service</h4>
                                    <p>Get a premium buying experience with us for your vehicle. We provide you with
                                        insurance and timely vehicle services.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="service_thumb">
                        <img src="{% static 'images/service/1.jpg' %}" alt="1.jpg">
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Our Testimonials -->
    <section class="our-testimonial bgc-f9">
        <div class="container">
            <div class="row">
                <div class="col-lg-6 offset-lg-3">
                    <div class="main-title text-center">
                        <h2>Our Testimonials</h2>
                    </div>
                </div>
            </div>
            <div class="row justify-content-center">
                <div class="col-lg-12">
                    <div class="home2_testimonial_tabs">
                        <div class="tab-content" id="pills-tabContent2">
                            <div class="tab-pane fade show active" id="review-1" role="tabpanel"
                                aria-labelledby="review-1-tab">
                                <div class="testimonial_post_home2 text-center">
                                    <div class="details">
                                        <p>I will personally recommend people to visit Dream CarBazaar because they are
                                            working consistently with their customers to provide the best deal. With
                                            them, you can purchase your dream car.</p>
                                    </div>
                                </div>
                            </div>
                            <div class="tab-pane fade" id="review-2" role="tabpanel" aria-labelledby="review-2-tab">
                                <div class="testimonial_post_home2 text-center">
                                    <div class="details">
                                        <p>Getting a car for our family was a big decision and Dream CarBazaar helped us
                                            to fulfil our dream of buying a Hyundai i20 on budget. My experience with
                                            them was amazing.</p>
                                    </div>
                                </div>
                            </div>
                            <div class="tab-pane fade" id="review-3" role="tabpanel" aria-labelledby="review-3-tab">
                                <div class="testimonial_post_home2 text-center">
                                    <div class="details">
                                        <p>I had many doubts before buying a second-hand car. But after visiting Dream
                                            CarBazaar and test-driving the Tata Nexon I didn’t even feel like I bought a
                                            second-hand car. </p>
                                    </div>
                                </div>
                            </div>
                            <div class="tab-pane fade" id="review-4" role="tabpanel" aria-labelledby="review-4-tab">
                                <div class="testimonial_post_home2 text-center">
                                    <div class="details">
                                        <p>Thanks to Dream CarBazaar I got the best price for my car. You get the best
                                            price for your used car. Their team is professional and all the paperwork is
                                            easy and hassle-free.</p>
                                    </div>
                                </div>
                            </div>
                            <div class="tab-pane fade" id="review-5" role="tabpanel" aria-labelledby="review-5-tab">
                                <div class="testimonial_post_home2 text-center">
                                    <div class="details">
                                        <p>Selling your old car has become easier with Dream CarBazaar. Sell your car
                                            within a few days and get a genuine price for your old vehicle. Everything
                                            is hassle-free complete your procedure through their website.</p>
                                    </div>
                                </div>
                            </div>
                            <div class="tab-pane fade" id="review-6" role="tabpanel" aria-labelledby="review-6-tab">
                                <div class="testimonial_post_home2 text-center">
                                    <div class="details">
                                        <p>We were planning to buy a Hyundai Creta for our family but considering the
                                            prices of the new vehicle we decided to buy a used car. That’s when we found
                                            out about Dream CarBazaar and trust me it’s worth buying a used car.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <ul class="nav justify-content-center mb-3" id="pills-tab2" role="tablist">
                            <li class="nav-item" role="presentation">
                                <a class="nav-link active" id="review-1-tab" data-bs-toggle="pill" href="#review-1"
                                    role="tab" aria-controls="review-1" aria-selected="true">
                                    <div class="thumb d-flex">
                                        <img class="rounded-circle" src="{% static 'images/dcb-boy.webp' %}"
                                            alt="1.jpg">
                                        <h4 class="title">Rahul Roy</h4>
                                    </div>
                                </a>
                            </li>
                            <li class="nav-item" role="presentation">
                                <a class="nav-link" id="review-2-tab" data-bs-toggle="pill" href="#review-2" role="tab"
                                    aria-controls="review-2" aria-selected="false">
                                    <div class="thumb d-flex">
                                        <img class="rounded-circle" src="{% static 'images/dcb-boy.webp' %}"
                                            alt="2.jpg">
                                        <h4 class="title">Vipul Saxena</h4>
                                    </div>
                                </a>
                            </li>
                            <li class="nav-item" role="presentation">
                                <a class="nav-link" id="review-3-tab" data-bs-toggle="pill" href="#review-3" role="tab"
                                    aria-controls="review-3" aria-selected="false">
                                    <div class="thumb d-flex">
                                        <img class="rounded-circle" src="{% static 'images/dcb-boy.webp' %}"
                                            alt="3.jpg">
                                        <h4 class="title">Ankit Singh</h4>
                                    </div>
                                </a>
                            </li>
                            <li class="nav-item" role="presentation">
                                <a class="nav-link active" id="review-4-tab" data-bs-toggle="pill" href="#review-4"
                                    role="tab" aria-controls="review-4" aria-selected="true">
                                    <div class="thumb d-flex">
                                        <img class="rounded-circle" src="{% static 'images/dcb-boy.webp' %}"
                                            alt="1.jpg">
                                        <h4 class="title">Pawan Yadav</h4>
                                    </div>
                                </a>
                            </li>
                            <li class="nav-item" role="presentation">
                                <a class="nav-link" id="review-5-tab" data-bs-toggle="pill" href="#review-5" role="tab"
                                    aria-controls="review-5" aria-selected="false">
                                    <div class="thumb d-flex">
                                        <img class="rounded-circle" src="{% static 'images/dcb-girl.webp' %}"
                                            alt="2.jpg">
                                        <h4 class="title">Anjali Singh</h4>
                                    </div>
                                </a>
                            </li>
                            <li class="nav-item" role="presentation">
                                <a class="nav-link" id="review-6-tab" data-bs-toggle="pill" href="#review-6" role="tab"
                                    aria-controls="review-6" aria-selected="false">
                                    <div class="thumb d-flex">
                                        <img class="rounded-circle" src="{% static 'images/dcb-girl.webp' %}"
                                            alt="3.jpg">
                                        <h4 class="title">Samayra Patnekar</h4>
                                    </div>
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>

    {% include 'Website/footer.html' %}

</div>
<!-- Wrapper End -->
{% endblock %}

{% block js %}

<script>
    $(document).ready(function() {
    console.log('sdfsdn')



    $('#car_brand').change(async function() {
        var brandID = $(this).val();
        console.log('brandID = ', brandID)
        await $.get('/get_car_model/', { car_brand_id: brandID }, async function(data) {
            var carModelSelect = $('#car_model');
            console.log('carModelSelect= ',carModelSelect)
            var model_text = '<option value="">Select Model</option>'
            await $.each(data, function(index, model) {
                console.log('data = ',data)
                var a = '<option value='+model.id+'>'+model.name+'</option>'
                model_text += a
<!--                carModelSelect.append('<option data-tokens="" value='+model.id+'>'+model.name+'</option>');-->
            });
             carModelSelect.html(model_text);

        });
    });

    $('#car_model').change(function() {
        var carModelId = $(this).val();
        $.get('/get_car_variant/', { car_model_id: carModelId }, function(data) {
            var carVariantSelect = $('#car_variants');
            carVariantSelect.empty();
            carVariantSelect.append($('<option>', {
                    value: "",
                    text: "Select Variants"
                }));
            $.each(data, function(index, variant) {
                carVariantSelect.append($('<option>', {
                    value: variant.id,
                    text: variant.name
                }));
            });
        });
    });
});

</script>


{% endblock %}