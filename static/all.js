var come_alert, coming, going, leave_alert;

coming = function() {
  return alert("Please buy something");
};

going = function() {
  return alert("Go back and buy more art!");
};

leave_alert = function() {
  var uri;
  uri = document.documentURI;
  if (uri.search('purchase') !== -1) {
    return going();
  }
};

come_alert = function() {
  var uri;
  uri = document.documentURI;
  if (uri.search('purchase') !== -1) {
    return coming();
  }
};
