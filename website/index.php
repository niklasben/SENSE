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

    <header>
        <hgroup>
            <h1>SENSE</h1>
            <h4>Supported sciENtific SEarch</h4>
        </hgroup>
        <nav>
            <h2>Nav h2</h2>
            <ul>
                <li>li 1</li>
                <li>li 2</li>
            </ul>
        </nav>
    </header>

    <section>
        <header>
                <h3>Texteingabe</h3>
        </header>

        <?php include ("form.php"); ?>

    </section>

    <aside>
        <header>
            <h3>Ergebnisse</h3>
        </header>

        <p>p aside</p>
    </aside>

    <br style="clear: both;" />

    <footer>
        <p>Author | Copyright | Contact</p>
        <time datetime="2016-09-10">10. September 2016</time>
    </footer>

</body>

</html>
