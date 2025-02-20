<!DOCTYPE html>
<html>
<html lang="de" />

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>SENSE (Supported sciENtific SEarch)</title>
    <!-- jQuery library -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <!-- Latest compiled JavaScript -->
    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" />
    <!-- CSS for page -->
    <link href="css/structure.css" rel="stylesheet" />
</head>

<body>

    <nav class="navbar navbar-default navbar-fixed-top">
        <div class="container-fluid">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">SENSE</a>
            </div>
            <div class="collapse navbar-collapse" id="myNavbar">
            <ul class="nav navbar-nav">
                <li class="active"><a href="#">Home</a></li>
                <!-- <li><a href="#">Page 1</a></li>
                <li><a href="#">Page 2</a></li>
                <li><a href="#">Page 3</a></li> -->
            </ul>
                <ul class="nav navbar-nav navbar-right">
                    <li>
                        <a href="#">
                            <span class="glyphicon glyphicon-user"></span> Sign Up
                        </a>
                    </li>
                    <li>
                        <a href="#">
                            <span class="glyphicon glyphicon-log-in"></span> Login
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <div class="container-fluid" style="margin-top: 75px; margin-bottom: 75px;">
        <div class="row">
            <div class="col-md-7">
                <?php include ("form.php"); ?>
            </div>
            <div class="col-md-5">
                <p class="bg-primary">Erkannte DDC:</p>
                <div class="row">
                    <div class="col-md-12">
                        <p class="bg-info">Ergebnisse - Chunks</p>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-12">
                        <p class="bg-info">Ergebnisse - NN</p>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-12">
                        <p class="bg-info">Ergebnisse - NE</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="clearfix"></div>
    <!-- <br style="clear: both;" /> -->

    <footer class="navbar navbar-default navbar-fixed-bottom">
        <div class="container">
            <p class="text-muted">
                <span class="glyphicon glyphicon-copyright-mark"></span> Author |
                <span class="glyphicon glyphicon-envelope"></span> Contact
            </p>
        </div>
        <!-- <time datetime="2016-09-10">10. September 2016</time> -->
    </footer>

</body>

</html>
