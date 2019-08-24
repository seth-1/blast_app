import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';

class NameForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  async handleSubmit(event) {
    // alert('A name was submitted: ' + this.state.value);
    const headers = new Headers();
    headers.append('Content-Type', 'application/json');

    const options = {
      method: 'POST',
      headers,
      body: JSON.stringify(this.state.value)
    };

    const request = new Request('http://localhost:8000/api/blast_request/', options);
    const response = await fetch(request);
    const status = response.status;
    console.log(response.status)

    if (status === 201){
      console.log("Enable update here.")
    }
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Dna sequence:
        </label>
          <textarea rows="4" cols="40" id="dna_input" type="text" value={this.state.value} onChange={this.handleChange} />
        <input type="submit" value="Submit" />
      </form>
    );
  }
}

class App extends Component {
  state = {
    blastruns: []
  };

  async componentDidMount(){
      const res = await fetch('http://localhost:8000/api/?format=json');
      const blastruns = await res.json();
      console.log(blastruns);
      this.setState({
        blastruns
      });
  }

  render() {
    return (
      <div>
      <div>
      <NameForm />
      </div>
      <div>
        {this.state.blastruns.map(item => (
          <div>
            <h3>Blast submission: {item.id}</h3>
            {item.results.map(sub => (
              <p>{sub}</p>
              ))}
          </div>
        ))}
      </div>
      </div>
    );
  }
}

// TODO: each child in list shold have unique key prop

export default App;
