var React = require('react');
var ReactRouter = require('react-router');
var Router = ReactRouter.Router;
var Route = ReactRouter.Route;
var IndexRoute = ReactRouter.IndexRoute;
var hashHistory = ReactRouter.hashHistory;
var NavbarContainer = require('../containers/navbarContainer');


var routes = (

    <Router history={hashHistory}>
        <Route path='/' component={NavbarContainer}>
        </Route>
    </Router>
);

module.exports = routes;