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





