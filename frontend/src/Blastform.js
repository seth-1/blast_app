import React, { Component } from 'react';

class BlastForm extends Component {
  constructor(props) {
    super(props);
    this.state = {value: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  canBeSubmitted() {
    const { value } = this.state;
    return value.length > 30;
  }

  async handleSubmit(event) {
    if (!this.canBeSubmitted()) {}
    alert('A DNA sequene was submitted: ' + this.state.value);
    const headers = new Headers();
    headers.append('Content-Type', 'application/json');

    const options = {
      method: 'POST',
      headers,
      body: JSON.stringify(this.state.value)
    };

    const request = new Request('http://localhost:8000/api/blast_request/', options);
    // const request = new Request('http://104.248.138.52:8000/api/blast_request/', options);
    const response = await fetch(request);
    const status = response.status;

    if (status === 200){
      console.log("Sequence processed.")
    }
    if (status === 400){
      console.log("Please provide a valid DNA sequence consisting of ATGC")
    }
    event.preventDefault();
  }

  render() {
    const isEnabled = this.canBeSubmitted();
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Dna sequence:
        </label>
          <textarea
          rows="4"
          cols="40"
          id="dna_input"
          placeholder="Enter a DNA sequence consisting of ATGC of at least length 30. It is advisable to at least use partial coding sequences to avoid stop codons."
          type="text"
          value={this.state.value}
          onChange={this.handleChange}
          />
        <input disabled={!isEnabled} type="submit" value="Submit" />
      </form>
    );
  }
}

export default BlastForm;