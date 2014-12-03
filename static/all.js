var app, come_alert, coming, going, leave_alert;

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

app = angular.module("myApp", []);

app.config([
  "$interpolateProvider", function($interpolateProvider) {
    $interpolateProvider.startSymbol("{[");
    return $interpolateProvider.endSymbol("]}");
  }
]).controller("EmailController", [
  "$scope", function($scope) {
    $scope.name = "your name";
    $scope.email = "youremail@something.com";
    $scope.subject = "your subject";
    $scope.body = "enter your order here!";
    return $scope.sendEmail = function() {
      return window.location = "mailto:drew.verlee@gmail.com?subject=" + $scope.subject + "&body=" + "Email: " + $scope.email + " -- name: " + $scope.name + " -- message: " + $scope.body;
    };
  }
]);

$(document).ready(function() {
  return $(".art_pieces").slick({
    infinite: true,
    slidesToShow: 2,
    slidesToScroll: 2
  });
});
