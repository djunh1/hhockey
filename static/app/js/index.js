

var React = require('react');
var ReactDOM = require('react-dom');
var Unassisted = React.createClass({
    render: function(){
        return (
         <div>
            Unassisted baby
         </div>
        )
    }
});
ReactDOM.render(<Unassisted />, document.getElementById('app'));
