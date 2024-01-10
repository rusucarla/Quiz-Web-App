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
//import backgroundImage from "https://assets.stickpng.com/thumbs/5845e614fb0b0755fa99d7e8.png";
const backgroundImageUrls = [
	"url('https://picsum.photos/2048/1024')",
	"url('https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/05df5aec-d346-43e9-b656-134e4dbce127/del1kiz-6838f412-466b-4080-b479-8ae8f1f9177a.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzA1ZGY1YWVjLWQzNDYtNDNlOS1iNjU2LTEzNGU0ZGJjZTEyN1wvZGVsMWtpei02ODM4ZjQxMi00NjZiLTQwODAtYjQ3OS04YWU4ZjFmOTE3N2EucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.gjs74O5vdVs4suhOlygYTf7iGBwfE3VuLdPfRwxj9YA')",
	"url('https://s3-prod.pionline.com/s3fs-public/ETF-Screen-Charts_i.jpg')",
	"url('https://cdn4.iconfinder.com/data/icons/bitcoin-mining-and-more/405/Asset_1240-512.png')",
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
			this.setState((prevState) => ({ score: prevState.score + 5 }));
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
		this.setState((prevState) => ({score: prevState.score + 5}))
	}
	if (current === 5)
	{
		if (select === "i am teddy bear")
		this.setState((prevState) => ({score: prevState.score - 20}))
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
          minHeight: "100vmin",
		  backgroundColor: "rgba(205, 250, 205, 0.5)",
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

