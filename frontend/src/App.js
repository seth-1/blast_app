import React, {Component} from 'react';
import './App.css';
import BlastList from './Blastlist';
import BlastForm from './Blastform'


class App extends Component {
  state = {
    blast : []
  };

  async componentDidMount(){
      const res = await fetch('http://localhost:8000/api/?format=json');
      // const res = await fetch('http://104.248.138.52:8000/api/?format=json');
      const blast = await res.json();
      this.setState({
        blast
      });
  }

  render() {
    let {blast} = this.state;
    return (
      <div>
      <div>
      <BlastForm />
      </div>
      <BlastList 
      blastData = {blast}
      />
      </div>
    );
  }
}

export default App;
