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

    <nav class="navbar navbar-inverse navbar-fixed-top">
        <div class="container-fluid">
            <div class="navbar-header">
                <a class="navbar-brand" href="#">SENSE</a>
            </div>
            <ul class="nav navbar-nav">
                <li class="active"><a href="#">Home</a></li>
                <li><a href="#">Page 1</a></li>
                <li><a href="#">Page 2</a></li>
                <li><a href="#">Page 3</a></li>
            </ul>
            <ul class="nav navbar-nav navbar-right">
                <li><a href="#"><span class="glyphicon glyphicon-user"></span> Sign Up</a></li>
                <li><a href="#"><span class="glyphicon glyphicon-log-in"></span> Login</a></li>
            </ul>
        </div>
    </nav>

    <section class="well">
        <header>
                <h3>Texteingabe</h3>
        </header>

        <?php include ("form.php"); ?>

    </section>

    <aside class="well">
        <header>
            <h3>Ergebnisse</h3>
        </header>

        <p>p aside</p>
    </aside>

    <br style="clear: both;" />

    <footer>
        <p>
            <span class="glyphicon glyphicon-copyright-mark"></span> Author |
            <span class="glyphicon glyphicon-envelope"></span> Contact
        </p>
        <time datetime="2016-09-10">10. September 2016</time>
    </footer>

</body>

</html>
