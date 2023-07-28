import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "business@kasyapi.com"
receiver_email = "fadhil.elsafer@gmail.com"
password = input("Masukan Password : ")

message = MIMEMultipart("alternative")
message["Subject"] = "Test_V.1.0.0"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
html = """
<html lang="en" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml">

<head>
    <title></title>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />
    <!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml><![endif]--><!--[if !mso]><!-->
    <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" type="text/css" /><!--<![endif]-->
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            padding: 0;
        }

        a[x-apple-data-detectors] {
            color: inherit !important;
            text-decoration: inherit !important;
        }

        #MessageViewBody a {
            color: inherit;
            text-decoration: none;
        }

        p {
            line-height: inherit
        }

        .desktop_hide,
        .desktop_hide table {
            mso-hide: all;
            display: none;
            max-height: 0px;
            overflow: hidden;
        }

        .image_block img+div {
            display: none;
        }

        @media (max-width:720px) {
            .desktop_hide table.icons-inner {
                display: inline-block !important;
            }

            .icons-inner {
                text-align: center;
            }

            .icons-inner td {
                margin: 0 auto;
            }

            .image_block img.fullWidth {
                max-width: 100% !important;
            }

            .social_block.desktop_hide .social-table {
                display: inline-block !important;
            }

            .row-content {
                width: 100% !important;
            }

            .stack .column {
                width: 100%;
                display: block;
            }

            .mobile_hide {
                max-width: 0;
                min-height: 0;
                max-height: 0;
                font-size: 0;
                display: none;
                overflow: hidden;
            }

            .desktop_hide,
            .desktop_hide table {
                max-height: none !important;
                display: table !important;
            }

            .row-2 .column-1 .block-3.text_block td.pad {
                padding: 10px !important;
            }

            .row-3 .column-2 .block-1.text_block td.pad {
                padding: 10px 10px 10px 20px !important;
            }

            .row-2 .column-1 .block-4.button_block a,
            .row-2 .column-1 .block-4.button_block div,
            .row-2 .column-1 .block-4.button_block span {
                font-size: 11px !important;
                line-height: 22px !important;
            }

            .row-3 .column-2 .block-3.text_block td.pad {
                padding: 10px 20px !important;
            }

            .row-6 .column-2 .block-1.text_block td.pad,
            .row-6 .column-2 .block-2.text_block td.pad {
                padding: 0 20px 10px !important;
            }

            .row-8 .column-1 .block-2.divider_block td.pad {
                padding: 10px !important;
            }

            .row-8 .column-1 .block-2.divider_block .alignment table {
                display: inline-table;
            }

            .row-13 .column-2 .block-1.image_block td.pad,
            .row-13 .column-3 .block-1.image_block td.pad {
                padding: 0 !important;
            }

            .row-16 .column-1 .block-1.text_block td.pad,
            .row-16 .column-1 .block-2.text_block td.pad,
            .row-16 .column-2 .block-1.text_block td.pad,
            .row-16 .column-2 .block-2.text_block td.pad {
                padding: 10px 10px 10px 20px !important;
            }

            .row-1 .column-1 {
                padding: 0 !important;
            }

            .row-14 .column-1,
            .row-14 .column-2 {
                padding: 5px 10px !important;
            }
        }
    </style>
</head>

<body style="text-size-adjust: none; background-color: #fff; margin: 0; padding: 0;">
    <table cellpadding="0" cellspacing="0" class="nl-container" role="presentation"
        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #fff;" width="100%">
        <tbody>
            <tr>
                <td>
                    <table cellpadding="0" cellspacing="0" class="row row-1" role="presentation"
                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table cellpadding="0" cellspacing="0" class="row-content stack" role="presentation"
                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff; color: #000; border-radius: 0; width: 700px; margin: 0 auto;"
                                        width="700">
                                        <tbody>
                                            <tr>
                                                <td class="column column-1"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="100%">
                                                    <table cellpadding="0" cellspacing="0" class="image_block block-1"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad" style="width:100%;">
                                                                <div class="alignment" style="line-height:10px"><img
                                                                        src="https://kasyapi.com/wp-content/uploads/2023/07/kop_email_yg_udah_bener_kasyapi.jpg"
                                                                        style="height: auto; display: block; border: 0; max-width: 700px; width: 100%;"
                                                                        width="700" /></div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table cellpadding="0" cellspacing="0" class="row row-2" role="presentation"
                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table cellpadding="0" cellspacing="0" class="row-content stack" role="presentation"
                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000; background-color: #f8f3ea; border-radius: 0; width: 700px; margin: 0 auto;"
                                        width="700">
                                        <tbody>
                                            <tr>
                                                <td class="column column-1"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="100%">
                                                    <div class="spacer_block block-1"
                                                        style="height:25px;line-height:25px;font-size:1px;"> </div>
                                                    <div class="spacer_block block-2"
                                                        style="height:25px;line-height:25px;font-size:1px;"> </div>
                                                    <table cellpadding="0" cellspacing="0" class="text_block block-3"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad">
                                                                <div style="font-family: sans-serif">
                                                                    <div class=""
                                                                        style="font-size: 12px; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; mso-line-height-alt: 18px; color: #393d47; line-height: 1.5;">
                                                                        <p
                                                                            style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 30px;">
                                                                            <span style="font-size:20px;"><strong>Presenting
                                                                                    by goods, for good
                                                                                    dealers</strong></span>
                                                                        </p>
                                                                    </div>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table cellpadding="10" cellspacing="0" class="button_block block-4"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad">
                                                                <div align="center" class="alignment">
                                                                    <!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="https://kasyapi.com/" style="height:34px;width:340px;v-text-anchor:middle;" arcsize="12%" stroke="false" fillcolor="#30a67a"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#ffffff; font-family:'Trebuchet MS', Tahoma, sans-serif; font-size:12px"><![endif]--><a
                                                                        href="https://kasyapi.com/"
                                                                        style="text-decoration:none;display:block;color:#ffffff;background-color:#30a67a;border-radius:4px;width:50%;border-top:0px solid #8a3b8f;font-weight:400;border-right:0px solid #8a3b8f;border-bottom:0px solid #8a3b8f;border-left:0px solid #8a3b8f;padding-top:5px;padding-bottom:5px;font-family:'Montserrat', 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif;font-size:12px;text-align:center;mso-border-alt:none;word-break:keep-all;"
                                                                        target="_blank"><span
                                                                            style="padding-left:5px;padding-right:5px;font-size:12px;display:inline-block;letter-spacing:normal;"><span
                                                                                style="word-break: break-word; line-height: 24px;">Our
                                                                                Website</span></span></a><!--[if mso]></center></v:textbox></v:roundrect><![endif]-->
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <div class="spacer_block block-5"
                                                        style="height:20px;line-height:20px;font-size:1px;"> </div>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table cellpadding="0" cellspacing="0" class="row row-3" role="presentation"
                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table cellpadding="0" cellspacing="0" class="row-content stack" role="presentation"
                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000; background-color: #f8f3ea; width: 700px; margin: 0 auto;"
                                        width="700">
                                        <tbody>
                                            <tr>
                                                <td class="column column-1"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; padding-bottom: 5px; padding-top: 5px; vertical-align: middle; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="33.333333333333336%">
                                                    <table cellpadding="0" cellspacing="0" class="image_block block-1"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad"
                                                                style="width:100%;padding-right:0px;padding-left:0px;">
                                                                <div class="alignment" style="line-height:10px"><img
                                                                        alt="I'm an image"
                                                                        src="http://drive.google.com/uc?export=view&id=1ikzE4Isf98wxBAL1i5Ky_IEUZv7i7AKQ"
                                                                        style="height: auto; display: block; border: 0; max-width: 93px; width: 100%;"
                                                                        title="I'm an image" width="93" /></div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                                <td class="column column-2"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; padding-bottom: 5px; padding-top: 5px; vertical-align: middle; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="66.66666666666667%">
                                                    <table cellpadding="10" cellspacing="0" class="text_block block-1"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad">
                                                                <div style="font-family: sans-serif">
                                                                    <div class=""
                                                                        style="font-size: 12px; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; mso-line-height-alt: 14.399999999999999px; color: #555555; line-height: 1.2;">
                                                                        <p
                                                                            style="margin: 0; font-size: 16px; text-align: left; mso-line-height-alt: 19.2px;">
                                                                            <span style="color:#393d47;"><strong>What
                                                                                    does Kasyapi do?</strong></span>
                                                                        </p>
                                                                    </div>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table cellpadding="10" cellspacing="0"
                                                        class="divider_block block-2" role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad">
                                                                <div class="alignment">
                                                                    <table cellpadding="0" cellspacing="0"
                                                                        role="presentation"
                                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                                        width="100%">
                                                                        <tr>
                                                                            <td class="divider_inner"
                                                                                style="font-size: 1px; line-height: 1px; border-top: 1px solid #BBBBBB;">
                                                                                <span></span>
                                                                            </td>
                                                                        </tr>
                                                                    </table>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table cellpadding="10" cellspacing="0" class="text_block block-3"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad"
                                                                style="padding-bottom:10px;padding-left:10px;padding-right:25px;">
                                                                <div class=""
                                                                    style="font-size: 12px; font-family: Montserrat; color: #555555; line-height: 2;">
                                                                    <p
                                                                        style="margin: 0; font-size: 12px; mso-line-height-alt: 28px;">
                                                                        KASYAPI
                                                                        Indonesia is one of the leading product
                                                                        spices and herbs suppliers from
                                                                        Indonesia based on Banda Aceh and
                                                                        Lhokseumawe. We continue to develop a
                                                                        wide range of products to meet customer
                                                                        demands, and helping our partners exceed
                                                                        their best abilities. We work alongside
                                                                        with farmers, producers, manufacturers,
                                                                        government and other organization to
                                                                        fulfill our goal of caring for the world
                                                                        in a safe, responsible and sustainable
                                                                        way
                                                                    </p>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table cellpadding="0" cellspacing="0" class="row row-4" role="presentation"
                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table cellpadding="0" cellspacing="0" class="row-content stack" role="presentation"
                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000; background-color: #f8f3ea; border-radius: 0; width: 700px; margin: 0 auto;"
                                        width="700">
                                        <tbody>
                                            <tr>
                                                <td class="column column-1"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="100%">
                                                    <div class="spacer_block block-1"
                                                        style="height:35px;line-height:35px;font-size:1px;"></div>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table cellpadding="0" cellspacing="0" class="row row-5" role="presentation"
                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table cellpadding="0" cellspacing="0" class="row-content stack" role="presentation"
                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000; background-color: #f8f3ea; width: 700px; margin: 0 auto;"
                                        width="700">
                                        <tbody>
                                            <tr>
                                                <td class="column column-1"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="100%">
                                                    <table cellpadding="0" cellspacing="0" class="image_block block-1"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad"
                                                                style="width:100%;padding-right:0px;padding-left:0px;">
                                                                <div class="alignment" style="line-height:10px"><img
                                                                        class="fullWidth"
                                                                        src="http://drive.google.com/uc?export=view&id=1LJET6I6ylxiCZ8BWA89sjBneZ90NxV-f"
                                                                        style="height: auto; display: block; border: 0; max-width: 700px; width: 100%;"
                                                                        width="700" /></div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <div class="spacer_block block-2"
                                                        style="height:30px;line-height:30px;font-size:1px;"> </div>
                                                    <table cellpadding="0" cellspacing="0" class="text_block block-3"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad"
                                                                style="padding-bottom:20px;padding-left:10px;padding-right:10px;padding-top:10px;">
                                                                <div style="font-family: sans-serif">
                                                                    <div class=""
                                                                        style="font-size: 14px; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; mso-line-height-alt: 16.8px; color: #393d47; line-height: 1.2;">
                                                                        <p dir="ltr"
                                                                            style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;">
                                                                            <strong><span style="font-size:30px;">Our
                                                                                    Commodity</span></strong>
                                                                        </p>
                                                                    </div>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table cellpadding="10" cellspacing="0"
                                                        class="divider_block block-4" role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad">
                                                                <div class="alignment">
                                                                    <table cellpadding="0" cellspacing="0"
                                                                        role="presentation"
                                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                                        width="25%">
                                                                        <tr>
                                                                            <td class="divider_inner"
                                                                                style="font-size: 1px; line-height: 1px; margin-right: 80px; border-top: 3px solid #30A67A;">
                                                                                <span> </span>
                                                                            </td>
                                                                        </tr>
                                                                    </table>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <div class="spacer_block block-5"
                                                        style="height:20px;line-height:20px;font-size:1px;"> </div>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table cellpadding="0" cellspacing="0" class="row row-6" role="presentation"
                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table cellpadding="0" cellspacing="0" class="row-content stack" role="presentation"
                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000; background-color: #f8f3ea; width: 700px; margin: 0 auto;"
                                        width="700">
                                        <tbody>
                                            <tr>
                                                <td class="column column-1"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="50%">
                                                    <table cellpadding="0" cellspacing="0" class="image_block block-1"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr><!--masukkan gambar1-->
                                                            <td class="pad"
                                                                style="width:100%;padding-right:0px;padding-left:0px;">
                                                                <div class="alignment" style="line-height:10px"><a
                                                                        style="outline:none" tabindex="-1"
                                                                        target="_blank"><img
                                                                            src="https://kasyapi.com/wp-content/uploads/2023/05/candle-nut2-min.png"
                                                                            style="height: auto; display: block; border: 0; max-width: 297.5px; width: 100%;"
                                                                            title="Alternate text" width="297.5" /></a>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <div class="spacer_block block-2"
                                                        style="height:20px;line-height:20px;font-size:1px;"> </div>
                                                    <table cellpadding="0" cellspacing="0" class="image_block block-3"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr> <!--masukkan gambar2-->
                                                            <td class="pad"
                                                                style="width:100%;padding-right:0px;padding-left:0px;">
                                                                <div class="alignment" style="line-height:10px"><a
                                                                        style="outline:none" tabindex="-1"
                                                                        target="_blank"><img
                                                                            src="https://kasyapi.com/wp-content/uploads/2023/05/candle-nut-min.png"
                                                                            style="height: auto; display: block; border: 0; max-width: 297.5px; width: 100%;"
                                                                            title="Alternate text" width="297.5" /></a>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                                <td class="column column-2"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="50%">
                                                    <table cellpadding="0" cellspacing="0" class="text_block block-1"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad"
                                                                style="padding-bottom:10px;padding-left:10px;padding-right:10px;">
                                                                <div style="font-family: sans-serif">
                                                                    <div class=""
                                                                        style="font-size: 12px; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; mso-line-height-alt: 24px; color: #393d47; line-height: 2;">
                                                                        <p
                                                                            style="margin: 0; font-size: 14px; mso-line-height-alt: 52px;">
                                                                            <span style="font-size:26px;"><strong><span
                                                                                        style="">Candlenut</span></strong></span>
                                                                        </p>
                                                                    </div>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table cellpadding="0" cellspacing="0" class="text_block block-2"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"
                                                        width="100%">
                                                        <tr><!--masukkan teks1-->
                                                            <td class="pad"
                                                                style="padding-bottom:10px;padding-left:10px;padding-right:25px;">
                                                                <div style="font-family: sans-serif">
                                                                    <div class=""
                                                                        style="font-size: 12px; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; mso-line-height-alt: 24px; color: #555555; line-height: 2;">
                                                                        <p
                                                                            style="margin: 0; font-size: 14px; mso-line-height-alt: 28px;">
                                                                            Candle nuts (Aleurites moluccana) are a
                                                                            relative of Macadamia nuts and resemble them
                                                                            in appearance and in texture.
                                                                        </p>
                                                                    </div>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <div class="spacer_block block-3 mobile_hide"
                                                        style="height:24px;line-height:24px;font-size:1px;"> </div>
                                                    <table cellpadding="0" cellspacing="0" class="html_block block-4"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad">
                                                                <div allign="center"
                                                                    style="font-family:Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;text-align:center;">
                                                                    <style>
                                                                        /* Apply left alignment to the table */
                                                                        .section-table table {
                                                                            border: 0px solid black;
                                                                            /* Adding a border for the entire table */
                                                                            margin-left: 0;
                                                                            /* Set left margin to 0 to align to the left */
                                                                            width: 100%;
                                                                            /* Make the table take up the full width of the container */
                                                                        }

                                                                        /* Add borders to each cell in the table */
                                                                        .section-table td {
                                                                            border: 1px solid black !important;
                                                                            padding: 5px !important;
                                                                            /* Optional: Adding padding for better spacing */
                                                                            text-align: left;
                                                                            /* Align the content to the left */
                                                                        }

                                                                        /* Create a container for the table */
                                                                        .table-container {
                                                                            margin-right: 26px;
                                                                            /* Right margin for desktop */
                                                                        }

                                                                        /* Responsive styles for mobile devices */
                                                                        @media (max-width: 600px) {
                                                                            .table-container {
                                                                                margin-right: 0;
                                                                                /* Remove right margin for mobile devices */
                                                                            }

                                                                            .section-table table {
                                                                                border-collapse: collapse;
                                                                                /* Collapse table borders for better display on small screens */
                                                                            }

                                                                            .section-table td {
                                                                                display: 0;
                                                                                /* Make table cells stack on top of each other */
                                                                                /*border: none;
                                                                                /* Remove cell borders for better display on small screens */
                                                                            }

                                                                            .table-container {
                                                                                margin-right: 26px;
                                                                                margin-left: 26px;
                                                                                /* margin for mobile*/
                                                                            }
                                                                        }
                                                                    </style>
                                                                    <div class="table-container section-table"
                                                                        style="overflow-x: auto;">
                                                                        <table>
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td>HS Code </td>
                                                                                    <td>080290</td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td>Color</td>
                                                                                    <td>Light Brown</td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td>Package</td>
                                                                                    <td>Meshbag 55cm x 95 cm (50kg)</td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td>Production Time</td>
                                                                                    <td>30 Days</td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td>Quantity</td>
                                                                                    <td>18 MT (MOQ)</td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td>Origin</td>
                                                                                    <td>Indonesia</td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                        <!--masukkan tabel html-->
                                                                    </div>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <div class="spacer_block"
                                                        style="height:24px;line-height:24px;font-size:1px;"> 
                                                    </div>
                                                    <table cellpadding="10" cellspacing="0" class="button_block block-6"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad">
                                                                <div class="alignment">
                                                                    <!--Masukkan teks whatsapp-->
                                                                    <!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="Https://wa.me/6285372603154?text=Hello%20there...%20Im%20interested%20to%20order%20cinnamon%20from%20you%20" style="height:42px;width:181px;v-text-anchor:middle;" arcsize="10%" stroke="false" fillcolor="#30a67a"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#ffffff; font-family:Tahoma, sans-serif; font-size:16px"><![endif]--><a
                                                                        href="Https://wa.me/6285372603154?text=Hello%20there...%20Im%20interested%20to%20order%20ginger%20from%20you%20"
                                                                        style="text-decoration:none;display:inline-block;color:#ffffff;background-color:#30a67a;border-radius:4px;width:auto;border-top:0px solid transparent;font-weight:400;border-right:0px solid transparent;border-bottom:0px solid transparent;border-left:0px solid transparent;padding-top:5px;padding-bottom:5px;font-family:Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;font-size:16px;text-align:center;mso-border-alt:none;word-break:keep-all;"
                                                                        target="_blank"><span
                                                                            style="padding-left:50px;padding-right:50px;font-size:16px;display:inline-block;letter-spacing:normal;"><span
                                                                                style="word-break: break-word; line-height: 32px;"><strong></strong></span>
                                                                            Order
                                                                            Now
                                                                            </strong></span></span></a>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table cellpadding="0" cellspacing="0" class="row row-7" role="presentation"
                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table cellpadding="0" cellspacing="0" class="row-content stack" role="presentation"
                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000; background-color: #f8f3ea; border-radius: 0; width: 700px; margin: 0 auto;"
                                        width="700">
                                        <tbody>
                                            <tr>
                                                <td class="column column-1"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="100%">
                                                    <div class="spacer_block block-1"
                                                        style="height:60px;line-height:60px;font-size:1px;"></div>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table cellpadding="0" cellspacing="0" class="row row-8" role="presentation"
                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table cellpadding="0" cellspacing="0" class="row-content stack" role="presentation"
                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000; background-color: #f8f3ea; border-radius: 8px 8px 0 0; width: 700px; margin: 0 auto;"
                                        width="700">
                                        <tbody>
                                            <tr>
                                                <td class="column column-1"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="100%">
                                                    <table cellpadding="0" cellspacing="0" class="heading_block block-1"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad"
                                                                style="padding-left:15px;padding-top:20px;text-align:center;width:100%;">
                                                                <h1
                                                                    style="margin: 0; color: #000000; direction: ltr; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; font-size: 32px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0;">
                                                                    <strong><span class="tinyMce-placeholder">We also
                                                                            Provide</span></strong>
                                                                </h1>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table cellpadding="10" cellspacing="0"
                                                        class="divider_block block-2" role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad">
                                                                <div allign="left" class="alignment">
                                                                    <table cellpadding="0" cellspacing="0"
                                                                        role="presentation"
                                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                                        width="50%">
                                                                        <tr>
                                                                            <td class="divider_inner"
                                                                                style="font-size: 1px; line-height: 1px; border-top: 2px solid #369478;">
                                                                                <span> </span>
                                                                            </td>
                                                                        </tr>
                                                                    </table>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table cellpadding="0" cellspacing="0" class="row row-9" role="presentation"
                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table cellpadding="0" cellspacing="0" class="row-content stack" role="presentation"
                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000; background-color: #f8f3ea; border-radius: 0; width: 700px; margin: 0 auto;"
                                        width="700">
                                        <tbody> <!--Masukan icon our product-->
                                            <tr>
                                                <td class="column column-1"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="25%">
                                                    <table cellpadding="0" cellspacing="0" class="image_block block-1"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad"
                                                                style="padding-left:15px;padding-right:15px;padding-top:15px;width:100%;">
                                                                <div class="alignment" style="line-height:10px"><img
                                                                        src="https://kasyapi.com/wp-content/uploads/2023/02/cinnamon.png"
                                                                        style="height: auto; display: block; border: 0; max-width: 145px; width: 100%;"
                                                                        width="145" /></div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table cellpadding="0" cellspacing="0" class="heading_block block-2"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad" style="text-align:center;width:100%;">
                                                                <h3
                                                                    style="margin: 0; color: #000000; direction: ltr; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; font-size: 16px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0;">
                                                                    <span class="tinyMce-placeholder">Cinnamon</span>
                                                                </h3>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                                <td class="column column-2"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="25%">
                                                    <table cellpadding="0" cellspacing="0" class="image_block block-1"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad"
                                                                style="padding-left:15px;padding-right:15px;padding-top:15px;width:100%;">
                                                                <div class="alignment" style="line-height:10px"><img
                                                                        src="https://kasyapi.com/wp-content/uploads/2023/02/ginger.png"
                                                                        style="height: auto; display: block; border: 0; max-width: 145px; width: 100%;"
                                                                        width="145" /></div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table cellpadding="0" cellspacing="0" class="heading_block block-2"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad" style="text-align:center;width:100%;">
                                                                <h1
                                                                    style="margin: 0; color: #000000; direction: ltr; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; font-size: 16px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0;">
                                                                    <span class="tinyMce-placeholder">Ginger</span>
                                                                </h1>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                                <td class="column column-3"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="25%">
                                                    <table cellpadding="0" cellspacing="0" class="image_block block-1"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad"
                                                                style="padding-left:15px;padding-right:15px;padding-top:15px;width:100%;">
                                                                <div class="alignment" style="line-height:10px"><img
                                                                        src="https://kasyapi.com/wp-content/uploads/2023/02/cloves.png"
                                                                        style="height: auto; display: block; border: 0; max-width: 145px; width: 100%;"
                                                                        width="145" /></div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table cellpadding="0" cellspacing="0" class="heading_block block-2"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad" style="text-align:center;width:100%;">
                                                                <h1
                                                                    style="margin: 0; color: #000000; direction: ltr; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; font-size: 16px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0;">
                                                                    <span class="tinyMce-placeholder">Cloves</span>
                                                                </h1>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                                <td class="column column-4"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="25%">
                                                    <table cellpadding="0" cellspacing="0" class="image_block block-1"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad"
                                                                style="padding-left:15px;padding-right:15px;padding-top:15px;width:100%;">
                                                                <div class="alignment" style="line-height:10px"><img
                                                                        src="	https://kasyapi.com/wp-content/uploads/2023/02/Black-Pepper.png"
                                                                        style="height: auto; display: block; border: 0; max-width: 145px; width: 100%;"
                                                                        width="145" /></div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table cellpadding="0" cellspacing="0" class="heading_block block-2"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad" style="text-align:center;width:100%;">
                                                                <h1
                                                                    style="margin: 0; color: #000000; direction: ltr; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; font-size: 16px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0;">
                                                                    <span class="tinyMce-placeholder">Black Peper</span>
                                                                </h1>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table cellpadding="0" cellspacing="0" class="row row-10" role="presentation"
                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table cellpadding="0" cellspacing="0" class="row-content stack" role="presentation"
                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000; background-color: #f8f3ea; border-radius: 0; width: 700px; margin: 0 auto;"
                                        width="700">
                                        <tbody>
                                            <tr>
                                                <td class="column column-1"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="100%">
                                                    <div class="spacer_block block-1"
                                                        style="height:25px;line-height:25px;font-size:1px;"> </div>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table cellpadding="0" cellspacing="0" class="row row-11" role="presentation"
                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table cellpadding="0" cellspacing="0" class="row-content stack" role="presentation"
                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000; background-color: #f8f3ea; border-radius: 0; width: 700px; margin: 0 auto;"
                                        width="700">
                                        <tbody>
                                            <tr>
                                                <td class="column column-1"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="25%">
                                                    <table cellpadding="0" cellspacing="0" class="image_block block-1"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad"
                                                                style="padding-left:15px;padding-right:15px;padding-top:15px;width:100%;">
                                                                <div class="alignment" style="line-height:10px"><a
                                                                        style="outline:none" tabindex="-1"
                                                                        target="_blank"><img
                                                                            src="https://kasyapi.com/wp-content/uploads/2023/02/pinenung.png"
                                                                            style="height: auto; display: block; border: 0; max-width: 145px; width: 100%;"
                                                                            width="145" /></a></div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table cellpadding="0" cellspacing="0" class="heading_block block-2"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad" style="text-align:center;width:100%;">
                                                                <h3
                                                                    style="margin: 0; color: #000000; direction: ltr; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; font-size: 16px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0;">
                                                                    <span class="tinyMce-placeholder">Betel Nut</span>
                                                                </h3>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                                <td class="column column-2"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="25%">
                                                    <table cellpadding="0" cellspacing="0" class="image_block block-1"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad"
                                                                style="padding-left:15px;padding-right:15px;padding-top:15px;width:100%;">
                                                                <div class="alignment" style="line-height:10px"><img
                                                                        src="https://kasyapi.com/wp-content/uploads/2023/02/Turmenic.png"
                                                                        style="height: auto; display: block; border: 0; max-width: 145px; width: 100%;"
                                                                        width="145" /></div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table cellpadding="0" cellspacing="0" class="heading_block block-2"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad" style="text-align:center;width:100%;">
                                                                <h1
                                                                    style="margin: 0; color: #000000; direction: ltr; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; font-size: 16px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0;">
                                                                    <span class="tinyMce-placeholder">Turmenic</span>
                                                                </h1>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                                <td class="column column-3"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="25%">
                                                    <table cellpadding="0" cellspacing="0" class="image_block block-1"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad"
                                                                style="padding-left:15px;padding-right:15px;padding-top:15px;width:100%;">
                                                                <div class="alignment" style="line-height:10px"><img
                                                                        src="https://kasyapi.com/wp-content/uploads/2023/02/Cardamom.png"
                                                                        style="height: auto; display: block; border: 0; max-width: 145px; width: 100%;"
                                                                        width="145" /></div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table cellpadding="0" cellspacing="0" class="heading_block block-2"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad" style="text-align:center;width:100%;">
                                                                <h1
                                                                    style="margin: 0; color: #000000; direction: ltr; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; font-size: 16px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0;">
                                                                    <span class="tinyMce-placeholder">Cardamom</span>
                                                                </h1>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                                <td class="column column-4"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="25%">
                                                    <table cellpadding="0" cellspacing="0" class="image_block block-1"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad"
                                                                style="padding-left:15px;padding-right:15px;padding-top:15px;width:100%;">
                                                                <div class="alignment" style="line-height:10px"><img
                                                                        src="https://kasyapi.com/wp-content/uploads/2023/03/ASEPTIC-COCONUT-MILK.png"
                                                                        style="height: auto; display: block; border: 0; max-width: 145px; width: 100%;"
                                                                        width="145" /></div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table cellpadding="0" cellspacing="0" class="heading_block block-2"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad" style="text-align:center;width:100%;">
                                                                <h1
                                                                    style="margin: 0; color: #000000; direction: ltr; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; font-size: 16px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0;">
                                                                    <span class="tinyMce-placeholder">Raw Derivied
                                                                        Coconut Product</span>
                                                                </h1>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table cellpadding="0" cellspacing="0" class="row row-12" role="presentation"
                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table cellpadding="0" cellspacing="0" class="row-content stack" role="presentation"
                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000; background-color: #f8f3ea; border-radius: 0; width: 700px; margin: 0 auto;"
                                        width="700">
                                        <tbody>
                                            <tr>
                                                <td class="column column-1"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="100%">
                                                    <div class="spacer_block block-1 mobile_hide"
                                                        style="height:75px;line-height:75px;font-size:1px;"> </div>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table cellpadding="0" cellspacing="0" class="row row-13" role="presentation"
                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table cellpadding="0" cellspacing="0" class="row-content stack" role="presentation"
                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000; background-color: #f8f3ea; width: 700px; margin: 0 auto;"
                                        width="700">
                                        <tbody>
                                            <tr>
                                                <td class="column column-1"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: center; font-weight: 400; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="33.333333333333336%">
                                                    <div class="spacer_block block-1"
                                                        style="height:20px;line-height:20px;font-size:1px;"> </div>
                                                    <table cellpadding="0" cellspacing="0" class="text_block block-2"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad"
                                                                style="padding-bottom: 20px; padding-left: 10px; padding-right: 10px; padding-top: 20px; text-align: center;">
                                                                <div style="font-family: sans-serif">
                                                                    <div class="title our journey mobile_hide"
                                                                        style="font-size: 14px; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; mso-line-height-alt: 21px; color: #393d47; line-height: 1.5;">
                                                                        <p
                                                                            style="margin: 0; font-size: 14px; mso-line-height-alt: 51px;">
                                                                            <span
                                                                                style="font-size: 34px; color: #30a57a;"><strong>Our<br>Journey</strong></span>
                                                                        </p>
                                                                    </div>
                                                                </div>
                                                                <div class="alignment"
                                                                    style="font-size: 14px; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; mso-line-height-alt: 21px; color: #393d47; line-height: 1.5;">
                                                                    <p class="Our Journey desktop_hide"
                                                                        style="margin: auto; font-size: 14px; font-size: 34px; color: #30a57a; mso-line-height-alt: 51px;">
                                                                        <strong>Our Journey</strong>
                                                                    </p>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                                <td class="column column-2"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; padding-bottom: 10px; padding-left: 10px; padding-right: 10px; padding-top: 10px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="33.333333333333336%">
                                                    <table cellpadding="0" cellspacing="0" class="image_block block-1"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad"
                                                                style="width:100%;padding-right:0px;padding-left:0px;">
                                                                <div class="alignment" style="line-height:10px"><img
                                                                        src="https://kasyapi.com/wp-content/uploads/2023/07/gudangpinang.gif"
                                                                        style="height: auto; display: block; border: 0; max-width: 213.33333333333331px; width: 100%;"
                                                                        width="213.33333333333331" /></div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                                <td class="column column-3"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; padding-bottom: 10px; padding-left: 10px; padding-right: 10px; padding-top: 10px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="33.333333333333336%">
                                                    <table cellpadding="0" cellspacing="0" class="image_block block-1"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad"
                                                                style="width:100%;padding-right:0px;padding-left:0px;">
                                                                <div class="alignment" style="line-height:10px"><img
                                                                        src="https://kasyapi.com/wp-content/uploads/2023/07/Kontainer.gif"
                                                                        style="height: auto; display: block; border: 0; max-width: 213.33333333333331px; width: 100%;"
                                                                        width="213.33333333333331" /></div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table cellpadding="0" cellspacing="0" class="row row-14" role="presentation"
                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table cellpadding="0" cellspacing="0" class="row-content stack" role="presentation"
                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000; background-color: #f8f3ea; border-radius: 0; width: 700px; margin: 0 auto;"
                                        width="700">
                                        <tbody>
                                            <tr>
                                                <td class="column column-1"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="50%">
                                                    <table cellpadding="0" cellspacing="0" class="image_block block-1"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad"
                                                                style="width:100%;padding-right:0px;padding-left:0px;">
                                                                <div class="alignment" style="line-height:10px"><img
                                                                        src="http://drive.google.com/uc?export=view&id=1isE0aYOuGzqR9CsSy8iafVb5NjMLMVQz"
                                                                        style="height: auto; display: block; border: 0; max-width: 315px; width: 100%;"
                                                                        width="315" /></div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                                <td class="column column-2"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="50%">
                                                    <table cellpadding="0" cellspacing="0" class="image_block block-1"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad"
                                                                style="width:100%;padding-right:0px;padding-left:0px;">
                                                                <div class="alignment" style="line-height:10px"><img
                                                                        src="https://kasyapi.com/wp-content/uploads/2023/07/ksjak.png"
                                                                        style="height: auto; display: block; border: 0; max-width: 315px; width: 100%;"
                                                                        width="315" /></div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table cellpadding="0" cellspacing="0" class="row row-15" role="presentation"
                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table cellpadding="0" cellspacing="0" class="row-content stack" role="presentation"
                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000; background-color: #f8f3ea; width: 700px; margin: 0 auto;"
                                        width="700">
                                        <tbody>
                                            <tr>
                                                <td class="column column-1"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="100%">
                                                    <div class="spacer_block block-1"
                                                        style="height:35px;line-height:35px;font-size:1px;"> </div>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table cellpadding="0" cellspacing="0" class="row row-16" role="presentation"
                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table cellpadding="0" cellspacing="0" class="row-content stack" role="presentation"
                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000; background-color: #f8f3ea; width: 700px; margin: 0 auto;"
                                        width="700">
                                        <tbody>
                                            <tr>
                                                <td class="column column-1"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; padding-bottom: 10px; padding-left: 10px; padding-right: 10px; padding-top: 10px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="50%">
                                                    <table cellpadding="0" cellspacing="0" class="text_block block-1"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad"
                                                                style="padding-bottom:10px;padding-left:25px;padding-right:10px;padding-top:10px;">
                                                                <div style="font-family: sans-serif">
                                                                    <div class=""
                                                                        style="font-size: 12px; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; mso-line-height-alt: 14.399999999999999px; color: #393d47; line-height: 1.2;">
                                                                        <p
                                                                            style="margin: 0; font-size: 18px; text-align: left; mso-line-height-alt: 21.599999999999998px;">
                                                                            <span style=""><strong><span style="">Social
                                                                                        media</span></strong></span>
                                                                        </p>
                                                                    </div>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table cellpadding="0" cellspacing="0" class="text_block block-2"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad"
                                                                style="padding-bottom:10px;padding-left:25px;padding-right:10px;padding-top:10px;">
                                                                <div style="font-family: sans-serif">
                                                                    <div class=""
                                                                        style="font-size: 12px; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; mso-line-height-alt: 18px; color: #717581; line-height: 1.5;">
                                                                        <p
                                                                            style="margin: 0; font-size: 14px; text-align: left; mso-line-height-alt: 18px;">
                                                                            <span style="font-size:12px;">Stay
                                                                                up-to-date with current activities and
                                                                                future events by following us,  Hope
                                                                                both of us can collaborate trought even
                                                                                more further</span>
                                                                        </p>
                                                                    </div>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table cellpadding="0" cellspacing="0" class="html_block block-3"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad">
                                                                <div
                                                                    style="font-family:Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;text-align:center;">
                                                                    <div style="height:20px;"> </div>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table cellpadding="0" cellspacing="0" class="social_block block-4"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad"
                                                                style="padding-left:20px;text-align:left;padding-right:0px;">
                                                                <div align="left" class="alignment">
                                                                    <table cellpadding="0" cellspacing="0"
                                                                        class="social-table" role="presentation"
                                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block;"
                                                                        width="126px">
                                                                        <td style="padding:0 10px 0 0;"><a
                                                                                href="https://facebook.com/"
                                                                                target="_blank"><img alt="Facebook"
                                                                                    height="32"
                                                                                    src="https://kasyapi.com/wp-content/uploads/2023/07/facebook2x-1.png"
                                                                                    style="height: auto; display: block; border: 0;"
                                                                                    title="Facebook" width="32" /></a>
                                                                        </td>
                                                                        <td style="padding:0 10px 0 0;"><a
                                                                                href="https://twitter.com/"
                                                                                target="_blank"><img alt="Twitter"
                                                                                    height="32"
                                                                                    src="https://kasyapi.com/wp-content/uploads/2023/07/twitter2x-1.png"
                                                                                    style="height: auto; display: block; border: 0;"
                                                                                    title="Twitter" width="32" /></a>
                                                                        </td>
                                                                        <td style="padding:0 10px 0 0;"><a
                                                                                href="https://instagram.com/"
                                                                                target="_blank"><img alt="Instagram"
                                                                                    height="32"
                                                                                    src="https://kasyapi.com/wp-content/uploads/2023/07/instagram2x-1.png"
                                                                                    style="height: auto; display: block; border: 0;"
                                                                                    title="Instagram" width="32" /></a>
                                                                        </td>
                                                                    </table>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                                <td class="column column-2"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; padding-bottom: 10px; padding-left: 10px; padding-right: 10px; padding-top: 10px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="50%">
                                                    <table cellpadding="0" cellspacing="0" class="text_block block-1"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad"
                                                                style="padding-bottom:10px;padding-left:25px;padding-right:10px;padding-top:10px;">
                                                                <div style="font-family: sans-serif">
                                                                    <div class=""
                                                                        style="font-size: 12px; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; mso-line-height-alt: 14.399999999999999px; color: #393d47; line-height: 1.2;">
                                                                        <p
                                                                            style="margin: 0; font-size: 18px; text-align: left; mso-line-height-alt: 21.599999999999998px;">
                                                                            <span style=""><strong><span style="">Where
                                                                                        to find
                                                                                        us</span></strong></span>
                                                                        </p>
                                                                    </div>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table cellpadding="0" cellspacing="0" class="text_block block-2"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad"
                                                                style="padding-bottom:10px;padding-left:25px;padding-right:10px;padding-top:10px;">
                                                                <div style="font-family: sans-serif">
                                                                    <div class=""
                                                                        style="font-size: 12px; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; mso-line-height-alt: 18px; color: #717581; line-height: 1.5;">
                                                                        <p
                                                                            style="margin: 0; mso-line-height-alt: 18px;">
                                                                            <span
                                                                                style="font-size:12px;">www.kasyapi.com</span>
                                                                        </p>
                                                                        <p
                                                                            style="margin: 0; mso-line-height-alt: 18px;">
                                                                            <span
                                                                                style="font-size:12px;">admin@kasyapi.com</span>
                                                                        </p>
                                                                        <p
                                                                            style="margin: 0; mso-line-height-alt: 18px;">
                                                                             </p>
                                                                        <p
                                                                            style="margin: 0; mso-line-height-alt: 18px;">
                                                                            <span style="font-size:12px;">Call us /
                                                                                Whatsapp<br />+62 853 7260
                                                                                3154<br /></span>
                                                                        </p>
                                                                    </div>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table cellpadding="0" cellspacing="0" class="text_block block-3"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad"
                                                                style="padding-bottom:10px;padding-left:25px;padding-right:10px;padding-top:10px;">
                                                                <div style="font-family: sans-serif">
                                                                    <div class=""
                                                                        style="font-size: 12px; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; mso-line-height-alt: 14.399999999999999px; color: #717581; line-height: 1.2;">
                                                                        <p
                                                                            style="margin: 0; font-size: 12px; mso-line-height-alt: 14.399999999999999px;">
                                                                             </p>
                                                                    </div>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table cellpadding="0" cellspacing="0" class="row row-17" role="presentation"
                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table cellpadding="0" cellspacing="0" class="row-content stack" role="presentation"
                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000; background-color: #f8f3ea; border-radius: 0 0 12px 12px; width: 700px; margin: 0 auto;"
                                        width="700">
                                        <tbody>
                                            <tr>
                                                <td class="column column-1"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="100%">
                                                    <div class="spacer_block block-1"
                                                        style="height:35px;line-height:35px;font-size:1px;"> </div>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table cellpadding="0" cellspacing="0" class="row row-18" role="presentation"
                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table cellpadding="0" cellspacing="0" class="row-content stack" role="presentation"
                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000; background-color: #fff; width: 700px; margin: 0 auto;"
                                        width="700">
                                        <tbody>
                                            <tr>
                                                <td class="column column-1"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="100%">
                                                    <div class="spacer_block block-1 mobile_hide"
                                                        style="height:40px;line-height:40px;font-size:1px;"> </div>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table cellpadding="0" cellspacing="0" class="row row-19" role="presentation"
                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table cellpadding="0" cellspacing="0" class="row-content stack" role="presentation"
                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000; background-color: #fff; width: 700px; margin: 0 auto;"
                                        width="700">
                                        <tbody>
                                            <tr>
                                                <td class="column column-1"
                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="100%">
                                                    <table cellpadding="0" cellspacing="0" class="icons_block block-1"
                                                        role="presentation"
                                                        style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                        width="100%">
                                                        <tr>
                                                            <td class="pad"
                                                                style="vertical-align: middle; color: #9d9d9d; font-family: inherit; font-size: 15px; padding-bottom: 5px; padding-top: 5px; text-align: center;">
                                                                <table cellpadding="0" cellspacing="0"
                                                                    role="presentation"
                                                                    style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;"
                                                                    width="100%">
                                                                    <tr>
                                                                        <td class="alignment"
                                                                            style="vertical-align: middle; text-align: center;">
                                                                            <!--[if vml]><table align="left" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]-->
                                                                            <!--[if !vml]><!-->
                                                                            <table cellpadding="0" cellspacing="0"
                                                                                class="icons-inner" role="presentation"
                                                                                style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block; margin-right: -4px; padding-left: 0px; padding-right: 0px;">
                                                                                <!--<![endif]-->
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </td>
            </tr>
        </tbody>
    </table><!-- End -->
</body>

</html>
"""

# Turn these into plain/html MIMEText objects
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("mail.kasyapi.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
