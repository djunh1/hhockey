var React = require('react');
var ReactRouter = require('react-router');
var Router = ReactRouter.Router;
var Route = ReactRouter.Route;
var IndexRoute = ReactRouter.IndexRoute;
var hashHistory = ReactRouter.hashHistory;
var LoginContainer = require('../containers/LoginContainer');


var routes = (

    <Router history={hashHistory}>
        <Route path='/account/login' component={LoginContainer}>
        </Route>
    </Router>
);

module.exports = routes;