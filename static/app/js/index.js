var React = require('react');
var ReactDOM = require('react-dom');
var routes = require('./config/routes');
var Raven = require('raven-js')


//Sentry Set up -  TODO
/*

// Get your keys by signing up for Sentry at sentry.reactjsprogram.com
var sentryKey = 'YOUR_SENTRY_KEY'
var sentryApp = 'YOUR_SENTRY_AP_ID'
var sentryURL = 'https://' + sentryKey + '@app.getsentry.com/' + sentryApp


//Release info, so we can check which release breaks.
var _APP_INFO = {
  name: 'Heritage Hockey',
  branch: 'master',
  version: '0.0'
}

Raven.config(sentryURL, {
  release: _APP_INFO.version,
  tags: {
    branch: _APP_INFO.branch,
    git_commit: ''
  }
}).install()


*/


ReactDOM.render(
    routes,
    document.getElementById('navapp')
);


/* jQUERY */


