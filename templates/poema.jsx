function getPoema() {
    return fetch('/poema/generator').then(data => data.json())
}
function Poema(props) {
    const [poema, setPoema] = useState({});
    useEffect(() => {
        getPoema().then(data => {
            setPoema(data);
        })
    }, []);
    return (
        <div>
            <button className="button" onClick={() => {
                getPoema().then(data => {
                    setPoema(data);
                })
            }}>
                <i className="material-icons">refresh</i>
            </button>
            <button className="button" onClick={() => {
                html2canvas(document.querySelector("html"), {
                    ignoreElements: function (element) {
                        if (element.classList.contains('button')) {
                            return true;
                        }
                    }
                }).then(canvas => {
                    var link = document.createElement('a');
                    link.download = 'feliz_dia.png';
                    link.href = canvas.toDataURL()
                    link.click();
                    // document.body.appendChild(canvas)
                });
            }}>
                <i className="material-icons">download</i>
            </button>
            <button className="button" onClick={() => {
                html2canvas(document.querySelector("html"), {
                    ignoreElements: function (element) {
                        if (element.classList.contains('button')) {
                            return true;
                        }
                    }
                }).then(canvas => {
                    fetch(canvas.toDataURL()).then(res => res.blob()).then(blob => {
                        let url = window.URL.createObjectURL(blob);
                        const file = new File([blob], 'feliz_dia.png', { type: 'image/png' });
                        navigator.share({ text: '', files: [file] });
                    })
                });

            }}>
                <i className="material-icons">share</i>
            </button>
            <div className="container">
                <h1 className="poema title">{poema.poema}</h1>
                <h2 className="poema">{poema.full}</h2>
            </div>
        </div>
    )
}