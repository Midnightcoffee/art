coming =() ->
  alert("Please buy something")

going =() ->
  alert("Go back and buy more art!")

leave_alert =() ->
  uri = document.documentURI
  if uri.search('purchase') != -1 then going()

come_alert =() ->
  uri = document.documentURI
  if uri.search('purchase') != -1 then coming()

app = angular.module("myApp", [])
app.config([
  "$interpolateProvider"
  ($interpolateProvider) ->
    $interpolateProvider.startSymbol "{["
    $interpolateProvider.endSymbol "]}"
]).controller "EmailController", [
  "$scope"
  ($scope) ->
    $scope.name = "your name"
    $scope.email = "youremail@something.com"
    $scope.subject = "your subject"
    $scope.body = "enter your order here!"
    $scope.sendEmail = ->
      window.location = "mailto:drew.verlee@gmail.com?subject=" + $scope.subject + "&body=" + "Email: " + $scope.email + " -- name: " + $scope.name + " -- message: " + $scope.body
]


$(document).ready ->
  $(".art_pieces").slick
    infinite: true
    slidesToShow: 2
    slidesToScroll: 2



