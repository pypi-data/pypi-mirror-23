var React = require('react');
var Bootstrap = require('react-bootstrap');
var Network = require('../network');
var connect = require('react-redux').connect;
var Reactable = require('reactable');

var Hosts = React.createClass({
    getInitialState: function () {
        return {hosts: [], loading: true};
    },
    getCurrentHosts: function () {
        var me = this;
        Network.post('/api/hosts', this.props.auth.token, {}).done(function (data) {
            me.setState({hosts: data.hosts, loading: false});
        }).fail(function (msg) {
            me.props.dispatch({type: 'SHOW_ALERT', msg: msg});
        });
    },
    componentDidMount: function () {
        this.getCurrentHosts();
    },
    deleteHost: function (e){
        var data = {"hostname": e.target.value};
        var me = this;
        Network.post('/api/hosts/delete', this.props.auth.token, data).done(function(data) {
            me.getCurrentHosts();
        }).fail(function (msg) {
            me.props.dispatch({type: 'SHOW_ALERT', msg: msg});
        });
    },
    addHost: function () {
        this.props.dispatch({type: 'OPEN_MODAL'});
    },
    render: function() {
        var host_rows = this.state.hosts.map(function(host) {
            var status = "", className = "";
            if(host.status.success){
                status = "Online";
            }else{
                popover = (
                    <Bootstrap.Popover title="Error">
                        {host.status.message}
                    </Bootstrap.Popover>
                );
                status = (<Bootstrap.OverlayTrigger overlay={popover}><a>Offline</a></Bootstrap.OverlayTrigger>);
                className = "danger";
            }
            return (
                <Reactable.Tr key={host.hostname} className={className}>
                    <Reactable.Td column="Host name">{host.hostname}</Reactable.Td>
                    <Reactable.Td column="IP">{host.host_ip}</Reactable.Td>
                    <Reactable.Td column="Instances">{host.instances.length}</Reactable.Td>
                    <Reactable.Td column="Driver">{host.driver_name}</Reactable.Td>
                    <Reactable.Td column="Status">{status}</Reactable.Td>
                    <Reactable.Td column="Actions"><Bootstrap.Button type="button" bsStyle='primary' onClick={this.deleteHost} value={host.hostname}>
                        Delete
                    </Bootstrap.Button></Reactable.Td>
                </Reactable.Tr>
            );
        }.bind(this));
        var NewHostFormRedux = connect(function(state){
            return {auth: state.auth, alert: state.alert, modal: state.modal};
        })(NewHostForm);
        var loading = this.state.loading;
        const spinnerStyle = {
            display: loading ? "block": "none",
        };
        const blockStyle = {
            visibility: loading ? "hidden": "visible",
        };
        return (<div className="app-containter">
            <NewHostFormRedux changeHosts = {this.getCurrentHosts} />
            <span className="spinner" style={spinnerStyle} ><i className="fa fa-spinner fa-spin fa-3x" aria-hidden="true"></i></span>
            <div style={blockStyle}>
                <Bootstrap.PageHeader>Current hosts <small>All specified hosts</small></Bootstrap.PageHeader>
                <Bootstrap.Button onClick={this.addHost} className="tbl-btn">
                    <Bootstrap.Glyphicon glyph='plus' />
                    Add host
                </Bootstrap.Button>
                <Reactable.Table className="table striped" columns={['Host name', 'IP', 'Instances', 'Driver', 'Status', 'Actions']} itemsPerPage={10} pageButtonLimit={10} noDataText="No matching records found." sortable={true} filterable={['Host name', 'IP', 'Instances', 'Driver', 'Status']} >
                    {host_rows}
                </Reactable.Table>
            </div>
        </div>);
    }
});

var HostStep = React.createClass({
    render: function () {
        var fields = [];
        for(var i = 0; i < this.props.fields.length; i++) {
            var field = this.props.fields[i];
            var formControl = null;
            var notAField = false;
            if(field.type === 'str') {
                formControl = <Bootstrap.FormControl type='text' key={field.id} id={field.id} value={this.props.fieldValues[field.id]} onChange={this.onChange} />;
            } else if(field.type === 'options') {
                formControl = (
                    <Bootstrap.FormControl componentClass='select' key={field.id} id={field.id} onChange={this.onChange}>
                        <option key={-1} value=''>Choose</option>
                        {this.props.optionChoices[field.id].map(function(option, i) {
                            return <option key={i} value={option}>{option}</option>
                        })}
                    </Bootstrap.FormControl>
                );
            } else if(field.type === 'description'){
                notAField = true;
                formControl = (
                    <Bootstrap.FormGroup key={field.id}>
                        <br/>
                        <Bootstrap.Well>
                            <h4>
                            {field.name} &nbsp;
                            <Bootstrap.Label bsStyle='info'> Info</Bootstrap.Label>
                            </h4>
                            <p>{this.props.optionChoices[field.id]}</p>
                        </Bootstrap.Well>
                    </Bootstrap.FormGroup>
                );
            }
            else if(field.type === 'file'){
                formControl = <Bootstrap.FormControl type='file' key={field.id} id={field.id} value={this.props.fieldValues[field.id]} onChange={this.onChange} />;
            }
            if(notAField) {
                fields.push(formControl);
            } else {
                fields.push(
                    <Bootstrap.FormGroup key={field.id}>
                        <Bootstrap.ControlLabel >{field.name}</Bootstrap.ControlLabel>
                        {formControl}
                    </Bootstrap.FormGroup>
                );
            }
        }
        return (
            <form>
                {fields}
            </form>
        )
    },
    onChange: function(e) {
        this.props.onFieldChange(e.target.id, e.target.value);
    }
});

var NewHostForm = React.createClass({
    getInitialState: function () {
        return {currentDriver: null, drivers: [], stepIndex: -1, optionChoices: {},
            errors: [], fieldValues: {}, isLoading: false};
    },
    componentDidMount: function () {
        var me = this;
        Network.get('/api/drivers', this.props.auth.token).done(function(data) {
            var newState = {drivers: data.drivers};
            me.setState(newState);
        }).fail(function (msg) {
            me.props.dispatch({type: 'SHOW_ALERT', msg: msg});
        });
    },
    onDriverSelect: function (e) {
        var driverId = e.target.value;
        for(var i = 0; i < this.state.drivers.length; i++){
            var driver = this.state.drivers[i];
            if(driver.id === driverId) {
                var fieldVals = {};
                var optionChoices = {};
                for(var j = 0; j < driver.steps.length; j++){
                    var step = driver.steps[j];
                    for(var k = 0; k < step.fields.length; k++){
                        var field = step.fields[k];
                        fieldVals[field.id] = '';
                        if(field.type == 'options' || field.type == 'description') {
                            optionChoices[field.id] = [];
                        }
                    }
                }
                this.setState({currentDriver: driver, stepIndex: -1, optionChoices: optionChoices,
                    errors: [], fieldValues: fieldVals});
                return;
            }
        }
        this.setState({currentDriver: null, stepIndex: -1, optionChoices: {},
            errors: [], fieldValues: {}});
    },
    onFieldChange: function(id, value){
        var newFieldValues = Object.assign({}, this.state.fieldValues);
        newFieldValues[id] = value;
        this.setState({fieldValues: newFieldValues});
    },
    close: function() {
        this.props.dispatch({type: 'CLOSE_MODAL'});
    },
    render: function () {
        var steps = [];
        var driverOptions = [<option key="-1" value=''>Select driver</option>];
        for(var i = 0; i < this.state.drivers.length; i++) {
            var driver = this.state.drivers[i];
            driverOptions.push(
                <option value={driver.id} key={driver.id}>{driver.friendly_name}</option>
            );
        }
        if(this.state.currentDriver !== null) {
            console.log(this.state.currentDriver);
            for(var j = 0; j < this.state.currentDriver.steps.length; j++){
                var step = this.state.currentDriver.steps[j];
                if(j !== this.state.stepIndex){
                    steps.push(
                        <Bootstrap.Tab title={step.name} eventKey={j} key={j} />
                    );
                }else{
                    steps.push(
                        <Bootstrap.Tab title={step.name} eventKey={j} key={j}>
                            <HostStep fields={step.fields} optionChoices={this.state.optionChoices}
                                fieldValues={this.state.fieldValues}
                                onFieldChange={this.onFieldChange}/>
                        </Bootstrap.Tab>
                    );
                }
            }
        }

        var errors = [];
        for(var i = 0; i < this.state.errors.length; i++){
            var err = this.state.errors[i];
            errors.push(
                <Bootstrap.Alert key={i} bsStyle='danger'>{err}</Bootstrap.Alert>
            );
        }

        var progressBar = null;
        if(this.state.isLoading) {
            progressBar = <Bootstrap.ProgressBar active now={100} />;
        }

        return (
            <Bootstrap.Modal show={this.props.modal.isOpen} onHide={this.close}>
                <Bootstrap.Modal.Header closeButton>
                  <Bootstrap.Modal.Title>Add host</Bootstrap.Modal.Title>
                </Bootstrap.Modal.Header>

                <Bootstrap.Modal.Body>
                    {progressBar}
                    <Bootstrap.Tabs id="add-host" activeKey={this.state.stepIndex}>
                        <Bootstrap.Tab title='Choose host' eventKey={-1}>
                            <Bootstrap.FormGroup controlId="formControlsSelect">
                                <Bootstrap.ControlLabel>Select host type</Bootstrap.ControlLabel>
                                <Bootstrap.FormControl componentClass="select" onChange={this.onDriverSelect} placeholder="select">
                                    {driverOptions}
                                </Bootstrap.FormControl>
                            </Bootstrap.FormGroup>
                        </Bootstrap.Tab>
                        {errors}
                        {steps}
                    </Bootstrap.Tabs>
                </Bootstrap.Modal.Body>

                <Bootstrap.Modal.Footer>
                    <Bootstrap.ButtonGroup>
                        <Bootstrap.Button disabled={this.state.isLoading} bsStyle='primary' onClick={this.nextStep}>
                            <Bootstrap.Glyphicon glyph='menu-right'></Bootstrap.Glyphicon> Next step</Bootstrap.Button>
                    </Bootstrap.ButtonGroup>
                </Bootstrap.Modal.Footer>
            </Bootstrap.Modal>);
    },
    nextStep: function () {
        if(this.state.currentDriver === null) return;
        if(this.state.stepIndex === -1){
            var me = this;
            var data = {driver_id: this.state.currentDriver.id, step_index: -1, field_values: {}};
            Network.post('/api/hosts/new/validate_fields', this.props.auth.token, data).done(function(d) {
                me.setState({stepIndex: d.new_step_index, optionChoices: d.option_choices});
            }).fail(function (msg) {
                me.props.dispatch({type: 'SHOW_ALERT', msg: msg});
            });
        } else {
            var me = this;
            me.setState({isLoading: true});
            var data = {driver_id: this.state.currentDriver.id, step_index: this.state.stepIndex,
                field_values: this.state.fieldValues};
            Network.post('/api/hosts/new/validate_fields', this.props.auth.token, data).done(function(d) {
                var mergeChoices = Object.assign({}, me.state.optionChoices);
                for(var id in d.option_choices){
                    mergeChoices[id] = d.option_choices[id];
                }
                if(d.new_step_index == -1 && d.errors.length == 0){
                    setTimeout(function(){
                         me.props.changeHosts();
                    }, 2000);
                }else{
                    me.setState({stepIndex: d.new_step_index, optionChoices: mergeChoices, errors: d.errors, isLoading: false});
                }
            }).fail(function (msg) {
                me.props.dispatch({type: 'SHOW_ALERT', msg: msg});
            });
            //var data = {driver_id: this.state.currentDriver.id, current_index: this.state.stepIndex,
            //}
        }
    },
    onSubmit: function(e) {
        e.preventDefault();
        var data = {name: this.refs.hostname.value, driver: this.state.currentDriver};
        var me = this;
        Network.post('/api/hosts', this.props.auth.token, data).done(function(data) {
            me.props.changeHosts();
        }).fail(function (msg) {
            me.props.dispatch({type: 'SHOW_ALERT', msg: msg});
        });
    }
});

Hosts = connect(function(state){
    return {auth: state.auth, alert: state.alert};
})(Hosts);

module.exports = Hosts;
