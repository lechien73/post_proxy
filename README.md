<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

A simple POST proxy to allow for redirection after a successful Zapier webhook submission.

## Usage

The following parameters can be set as the `name` attribute in hidden form fields:

`x_webhook` - the URL of the webhook to send the data to

`x_success` - the URL to redirect to after successful submission

`x_failure` - the URL to redirect to after an error

You can also specify these as environment variables on the host. If you want to do that, the expected variable names are:

`ZAPIER_WEBHOOK`

`SUCCESS_URL`

`FAILURE_URL`

Here is an example of a form with the hidden fields set:

```html
<form id="myForm" method="POST" action="https://(POST PROXY URL)">
    <input
        type="hidden"
        name="x_webhook"
        value="https://zapier.com/hooks/catch/12345/"
    />
    <input
        type="hidden"
        name="x_success"
        value="https://lechien73.github.io/new_test/thankyou.html"
    />
    <input
        type="hidden"
        name="x_failure"
        value="https://lechien73.github.io/new_test/error.html"
    />

    <!--- Rest of the form --->
</form>
```

Substitute your own values for _(POST PROXY URL)_ and the success and failure URLs.

---

Matt Rudge

June, 2020
