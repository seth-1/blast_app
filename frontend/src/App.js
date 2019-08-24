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

  handleSubmit(event) {
    alert('A name was submitted: ' + this.state.value);
    // fetch('/api/form-submit-url', {
    //   method: 'POST',
    //   body: this.state.value,
    // });
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Dna sequence:
          <input type="text" value={this.state.value} onChange={this.handleChange} />
        </label>
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
            <h3>{item.query_id}</h3>
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
// TODO: BLAST submission field

export default App;
