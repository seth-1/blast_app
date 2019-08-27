import React, { Component } from 'react';

const BlastListBody = props => { 
    const rows = props.blastData.map((row, index) => {
        return (
            <ul key={index}>
            {row.id}
            {row.results.map((sub, index) => (
              <li key={index}>{sub}</li>
              ))}
            </ul>
        );
    });

    return <div>{rows}</div>;
}

class BlastList extends Component {
    render() {
        const { blastData } = this.props;

        return (
            <div>
                <BlastListBody blastData={blastData} />
            </div>
        );
    }
}

export default BlastList;