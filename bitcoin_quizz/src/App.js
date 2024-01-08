// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;

// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
// import React, { Component } from "react";
// import "bootstrap/dist/css/bootstrap.min.css";
// import Question from "./Components/Question";
// import quests from "./Components/QuestionBank";
// import Score from "./Components/Score";
// import "./App.css";



import React, { Component } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import Question from "./Components/Question";
import qBank from "./Components/QuestionBank";
import Score from "./Components/Score";
import "./App.css";
import Fireworks from "react-fireworks";
//import backgroundImage from "https://assets.stickpng.com/thumbs/5845e614fb0b0755fa99d7e8.png";
const backgroundImageUrls = [
	"url('https://assets.stickpng.com/thumbs/5845e614fb0b0755fa99d7e8.png')",
	"url('https://assets.stickpng.com/thumbs/58967e9b0803320bf17c2fb8.png')",
	"url('https://assets.stickpng.com/thumbs/589b561082250818d81e7490.png')",
	"url('https://assets.stickpng.com/thumbs/5ee7713799588c0004aa6848.png')",
	"url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1mnnnHu9F_eY9hpUy3D0wt8_-FrwMWvmGlA&usqp=CAU')",
	"url('https://www.pngmart.com/files/22/Racoon-PNG.png')"
];
	//"https://assets.stickpng.com/thumbs/5ee7713799588c0004aa6848.png",
	//"https://assets.stickpng.com/thumbs/5ee771dc99588c0004aa6849.png"
 // ];
class App extends Component {
	constructor(props) {
		super(props);
		this.state = {
			questionBank: qBank,
			current: 0,
			select: "",
			score: 0,
			ender: false,
			fire: false,
		};
	}

	handleOptionChange = (e) => {
		this.setState({ select: e.target.value });
	};

	handleFormSubmit = (e) => {
		e.preventDefault();
		this.checkAnswer();
		this.NextQ();
		
	};

	checkAnswer = () => {
		const { questionBank, current, select, score } = this.state;
    const currentObj = questionBank[current];
    if (currentObj.hasOwnProperty("answer")){
      console.log("are");
      if (select === questionBank[current].answer) {
			this.setState((prevState) => ({ score: prevState.score + 1 }));
      console.log(score);
		}
    }
	if (current === 0) //e prima intrebare
	{
		console.log("hey");
		if (select === "YES")
			this.setState((prevState) => ({ score: prevState.score + 2 }));
		if (select === "i am already rich")
			this.setState((prevState) => ({score: prevState.score - 2}))
			if (select === "no, i like poverty")
			this.setState((prevState) => ({ score: prevState.score -3 }));
	}
	if (current === 1)
	{
		if (select === "angel clean")
			this.setState((prevState) => ({score: prevState.score + 1}));
		if (select === "corporate clean")
			this.setState((prevState) => ({score: prevState.score + 2}));
		if (select === "some like it hot...")
		    this.setState((prevState) => ({score: prevState.score + 3}));
		if (select === "i don't have a soul")
		this.setState((prevState) => ({score: prevState.score + 4}));
		}
	if (current === 4)
	{
		if (select === "My cat is God")
		this.setState((prevState) => ({score: prevState.score + 1}))
	}
	if (current === 5)
	{
		if (select === "i am teddy bear")
		this.setState((prevState) => ({score: prevState.score - 1}))
		if (select === "bullish!")
		this.setState((prevState) => ({score: prevState.score + 5}))
	}
		
	};

	NextQ = () => {
		const { questionBank, current } = this.state;
		if (current + 1 < questionBank.length) {
			this.setState((prevState) => ({
				current: prevState.current + 1,
				select: "",
			}));
		} else {
			this.setState({
				ender: true,
			});
		}
	};

	render() {
		const { questionBank, current, select, score, ender } =
			this.state;
		
		const backgroundImageUrl = backgroundImageUrls[current]
		return (
			<div   style={{
				textAlign: "center",
          fontFamily: "Arial, sans-serif",
		  backgroundImage: backgroundImageUrl,
          backgroundSize: "cover",
          backgroundPosition: "center",
          minHeight: "100vh",
			  }}className="App d-flex flex-column align-items-center justify-content-center">
				< h1
          style={{
            fontSize: "2em",
            marginBottom: "20px",
            color: "#ff00bb",
          }}className="app-title">Bitcoin quizz</h1>
				{!ender ? (
          
					<Question
						question={questionBank[current]}
						select={select}
						onOptionChange={this.handleOptionChange}
						onSubmit={this.handleFormSubmit}
						style={{
							border: "1px solid #ccc",
							padding: "20px",
							borderRadius: "5px",
							marginBottom: "20px",
							backgroundColor: "#ff0033",
						  }}
						  className="question-box"
					/>
				) : (
					<Score
						score={score}
						onNextQuestion={this.NextQ}
						style={{
							fontSize: "1.5em",
							marginTop: "30px",
							color: "##ff0033"
						  }}
						className="score"
					/>
				)}
			</div>
		);
	}
}

export default App;

