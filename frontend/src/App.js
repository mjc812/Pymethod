import './App.css';
import React from 'react';

function App() {

    const uploadFile = (e) => {
      const file = e.target.files[0];
      const data = new FormData();
      data.append('file', file);
        
      console.log(data.get('file'))

      fetch("http://127.0.0.1:5000/getmsg/?name=debbie", {
        method: 'POST',
        body: data
      })
      .then(res => res.json())
      .then(
        (result) => {},
        (error) => {}
      )
  }

  return (
      <div>
        <form>
          <input type="file" onChange={uploadFile}/>
        </form>
      </div>
  );
}

export default App;

