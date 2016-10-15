var React = require('react')

var NavbarContainer = React.createClass({
    render: function () {
        return (
            <div className="row">
                                <div className="col-lg-2 col-md-2 col-sm-12 co-xs-12">
                                    <div className="header-logo">
                                        <a href="index.html"> <img src="http://placehold.it/100x75" alt="logo" />
											 </a>
                                        <span className="nav-trigger toggle-hover visible-xs">
                                            <a className="toggle-icon fa fa-bars" href="#"> </a>
                                        </span>
                                    </div>
                                </div>
                                <div className="col-lg-9 col-md-10 col-sm-12 navigation font-2">
                                    <nav>
                                        <div className="navbar-collapse no-padding" id="primary-navigation">
                                            <span className="nav-trigger toggle-hover visible-xs">
                                                <a className="toggle-icon fa fa-times" href="#"> </a>
                                            </span>
                                            <ul className="nav navbar-nav primary-navbar">
                                                <li>
                                                    <a href="{% url 'home_page' %}"  aria-haspopup="true" >Home</a>
                                                </li>
                                             	<li>
                                                    <a href="#"  aria-haspopup="true" >Membership</a>
                                                </li>
                                                <li><a href="#">Our Sticks <sup className="bubble font-1">
                                                <span className="hot-tag">New</span> </sup></a></li>

                                                <li><a href="{% url 'about_page' %}">About Us</a></li>
                                             	<li><a href="{% url 'faq_page' %}">How it works</a></li>
												<li><a href="about-us.html">Login</a></li>
												<li><a href="about-us.html">Sign Up</a></li>

                                            <li className="cart-hover">
                                                <a href="#">Bag &nbsp;&nbsp;
                                                <span className="fa fa-shopping-cart"></span>
                                                <span className="items-count font-1"> 2 </span> </a>
                                                <div className="pop-up-box cart-style-1">
                                                    <div class="cart-title block-inline">
                                                        <h2 className="title-1">My Cart</h2>
                                                        <span className="fa fa-shopping-cart"></span>
                                                         <i className="items-count font-1"> 2 </i>
                                                    </div>
                                                    <div className="cart-item">
                                                        <div className="cart-list">
                                                            <div className="cart-img">
                                                            <img src="assets/img/product/cart-thumb-1.png" alt=""/>
                                                            </div>
                                                            <div className="cart-detail">
                                                                <a className="prod-title block-inline" href="#"> some shop item title </a>
                                                                <p className="fsz-16 font-2 no-margin">
                                                                    <span className="fw-300 gray-clr"> 2 <sub>X</sub> </span> $250.00
                                                                </p>
                                                            </div>
                                                        </div>
                                                        <div className="cart-list">
                                                            <div className="cart-img">
                                                            <img src="assets/img/product/cart-thumb-2.png" alt=""/> </div>
                                                            <div className="cart-detail">
                                                                <a className="prod-title block-inline" href="#"> some shop item title </a>
                                                                <p className="fsz-16 font-2 no-margin">
                                                                    <span className="fw-300 gray-clr"> 1 <sub>X</sub> </span> $250.00
                                                                </p>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div className="font-2 fsz-16 cart-total clearfix">
                                                        <div className="col-sm-5 col-xs-5"> Go To: </div>
                                                        <div className="col-sm-7 col-xs-7"> Total: $750.00 </div>
                                                    </div>
                                                    <div className="block-inline cart-btns">
                                                        <ul className="prod-meta">
                                                            <li> <a className="fa fa-heart meta-icon" href="#"></a> </li>
                                                            <li> <a className="fa fa-retweet meta-icon" href="#"></a> </li>
                                                            <li> <a className="theme-btn btn-black" href="#"> add to cart </a> </li>
                                                        </ul>
                                                    </div>
                                                </div>
                                            </li>
                                           </ul>
                                        </div>
                                    </nav>
                                </div>
                            </div>
        )
    }
});

module.exports = NavbarContainer;