var term,
    protocol,
    socketURL,
    socket,
    pid,
    charWidth,
    charHeight,
    path,
    curFont;

var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/x-www-form-urlencoded");

var terminalContainer = document.getElementById('terminal-container');

function setTerminalSize () {
  var cols = parseInt(colsElement.value, 10),
      rows = parseInt(rowsElement.value, 10),
      width = (cols * charWidth).toString() + 'px',
      height = (rows * charHeight).toString() + 'px';

  terminalContainer.style.width = width;
  terminalContainer.style.height = height;
  term.resize(cols, rows);
}

window.onresize = function(event) {
    term.fit();
}


createTerminal();

function createTerminal() {
  console.log("Creating term...");
  // Clean terminal
  while (terminalContainer.children.length) {
    terminalContainer.removeChild(terminalContainer.children[0]);
  }
  term = new Terminal({
    cursorBlink: true,
    scrollback: 10000,
    tabStopWidth: 10
  });

  term.on('resize', function (size) {
    if (!pid) {
      return;
    }
    term.fit();
    var cols = size.cols,
        rows = size.rows,
        url = '/api/terminals/' + pid + '/size?cols=' + cols + '&rows=' + rows;

    fetch(url, {method: 'POST', headers: myHeaders});
  });
  protocol = (location.protocol === 'https:') ? 'wss://' : 'ws://';
  socketURL = protocol + location.hostname + ((location.port) ? (':' + location.port) : '') + '/terminals/';

  term.open(terminalContainer);
  term.fit();
  term.toggleFullscreen(true);

  var initialGeometry = term.proposeGeometry(),
      cols = initialGeometry.cols,
      rows = initialGeometry.rows;
  console.log(cols);
  console.log(rows);


  fetch('/api/terminals?cols=' + cols + '&rows=' + rows, {method: 'POST', headers: myHeaders}).then(function (res) {

    charWidth = Math.ceil(term.element.offsetWidth / cols);
    charHeight = Math.ceil(term.element.offsetHeight / rows);

    res.text().then(function (pid) {
      term.fit()
      window.pid = pid;
      socketURL += pid;
      socket = new WebSocket(socketURL);
      socket.onopen = runRealTerminal;
      socket.onclose = closeTerm;
      socket.onerror = closeTerm;
    });
  });
}

function setFont(font) {
   fonts = "'ubuntu-powerline', monospace";
   fonts = "'"+font+"', "+fonts;
   $('.terminal').css('font-family', fonts);
   term.fit();
   var initialGeometry = term.proposeGeometry(),
       cols = initialGeometry.cols,
       rows = initialGeometry.rows;
   console.log(cols);
   console.log(rows);
}

function fitFont(font) {
    curFont = font;
    setFont(font);
    setFont('ubuntu-powerline');
    setFont(font);
}

function setcwd(cwd) {
  console.log(cwd);
  path = cwd;
}

function chdir(path) {
  term.send('cd '+path+'\n');
}

function clearTerm()
{
  term.send('clear\n');
}

function exec(cmd)
{
  term.send(''+cmd+'\n');
}

function closeTerm() {
  console.log("Closed via server");
  term.writeln("Pipe closed");
}

function consoleReady() {
  return term._initialized
}

function scrollTerm(delta) {
  var viewport = $('.xterm-viewport');
  var curScrollPos = viewport.scrollTop();
  var maxHeight = viewport.prop('scrollHeight') - viewport.innerHeight();
  curScrollPos = Math.min(maxHeight, Math.max(0, curScrollPos - delta));
  $('.xterm-viewport').animate({ scrollTop: curScrollPos }, 0);
}

function runRealTerminal() {
  term.attach(socket);
  console.log("Am I Alive?");
  term._initialized = true;
  term.writeln("Loading...");
  chdir(path);
  clearTerm();
  fitFont(curFont);
}
