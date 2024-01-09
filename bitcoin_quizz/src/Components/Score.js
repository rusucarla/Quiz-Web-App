import React, { Component } from 'react';
import '../App.css'
class Score extends Component {
    render() {
        const { score, onNextQuestion } = this.props;
        let imgsrc, message;
        if (score < 0) {
            imgsrc = 'https://s2.coinmarketcap.com/static/img/coins/200x200/24747.png';
            message = 'Negative Score';
        } else if (score >= 0 && score <= 3) {
            imgsrc = 'https://image.coinpedia.org/wp-content/uploads/2023/12/02174423/pepe.webp';
            message = 'Bitcoin';
        } else if (score > 3 && score < 5) {
            imgsrc = 'https://images.mktw.net/im-333859/social';
            message = '5 to 10 Score';
        } else if (score >= 5 && score <= 15) {
            imgsrc = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Bitcoin_logo.svg/1024px-Bitcoin_logo.svg.png';
            message = '10 to 15 Score';
        } else {
            imgsrc = 'https://pbs.twimg.com/media/Du11cdiWwAApx3q.jpg';
            message = 'Default Image';
        }
        return (
            <div>
                <h2>Results</h2>
                <h4>Your score: {score}</h4>
                
                <img src = {imgsrc} alt={message}/>
            </div>
        );
    }
}
 
export default Score;