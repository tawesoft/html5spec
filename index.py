{
    'attributes':
    [
        <class 'tuple'>:('abbr', {'th'}, 'Alternative label to use for the header cell when referencing the cell in other contexts', 'Text. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('accept', {'input'}, 'Hint for expected file type in file upload controls', 'Set of comma-separated tokens* consisting of valid MIME type strings with no parameters or audio/*, video/*, or image/. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('accept-charset', {'form'}, 'Character encodings to use for form submission', 'ASCII case-insensitive match for "UTF-8"', set()),
        <class 'tuple'>:('accesskey', {'HTML'}, 'Keyboard shortcut to activate or focus element', 'Ordered set of unique space-separated tokens, case-sensitive, consisting of one code point in length', set()),
        <class 'tuple'>:('action', {'form'}, 'URL to use for form submission', 'Valid non-empty URL potentially surrounded by spaces', set()),
        <class 'tuple'>:('allow', {'iframe'}, "Feature policy to be applied to the iframe's contents", 'Serialized feature policy', set()),
        <class 'tuple'>:('allowfullscreen', {'iframe'}, "Whether to allow the iframe's contents to use requestFullscreen()", 'Boolean attribute', set()),
        <class 'tuple'>:('allowpaymentrequest', {'iframe'}, "Whether the iframe's contents are allowed to use the PaymentRequest interface to make payment requests", 'Boolean attribute', set()),
        <class 'tuple'>:('alt', {'area', 'img', 'input'}, 'Replacement text for use when images are not available', 'Text. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('as', {'link'}, 'Potential destination for a preload request (for rel="preload" and rel="modulepreload")', 'Potential destination, for rel="preload"; script-like destination, for rel="modulepreload"', set()),
        <class 'tuple'>:('async', {'script'}, 'Execute script when available, without blocking while fetching', 'Boolean attribute', set()),
        <class 'tuple'>:('autocapitalize', {'HTML'}, 'Recommended autocapitalization behavior (for supported input methods)', '"on"; "off"; "none"; "sentences"; "words"; "characters"', {'"characters', '"sentences', '"off', '"none', '"words', 'on'}),
        <class 'tuple'>:('autocomplete', {'form'}, 'Default setting for autofill feature for controls in the form', '"on"; "off"', {'"off', 'on'}),
        <class 'tuple'>:('autocomplete', {'select', 'input', 'textarea'}, 'Hint for form autofill feature', 'Autofill field name and related tokens. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('autofocus', {'select', 'input', 'textarea', 'button'}, 'Automatically focus the form control when the page is loaded', 'Boolean attribute', set()),
        <class 'tuple'>:('autoplay', {'video', 'audio'}, 'Hint that the media resource can be started automatically when the page is loaded', 'Boolean attribute', set()),
        <class 'tuple'>:('charset', {'meta'}, 'Character encoding declaration', '"utf-8"', {'utf-8'}),
        <class 'tuple'>:('checked', {'input'}, 'Whether the control is checked', 'Boolean attribute', set()),
        <class 'tuple'>:('cite', {'ins', 'del', 'blockquote', 'q'}, 'Link to the source of the quotation or more information about the edit', 'Valid URL potentially surrounded by spaces', set()),
        <class 'tuple'>:('class', {'HTML'}, 'Classes to which the element belongs', 'Set of space-separated tokens', set()),
        <class 'tuple'>:('color', {'link'}, 'Color to use when customizing a site\'s icon (for rel="mask-icon")', 'CSS <color>', set()),
        <class 'tuple'>:('cols', {'textarea'}, 'Maximum number of characters per line', 'Valid non-negative integer greater than zero', set()),
        <class 'tuple'>:('colspan', {'th', 'td'}, 'Number of columns that the cell is to span', 'Valid non-negative integer greater than zero', set()),
        <class 'tuple'>:('content', {'meta'}, 'Value of the element', 'Text. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('contenteditable', {'HTML'}, 'Whether the element is editable', '"true"; "false"', {'"false', 'true'}),
        <class 'tuple'>:('controls', {'video', 'audio'}, 'Show user agent controls', 'Boolean attribute', set()),
        <class 'tuple'>:('coords', {'area'}, 'Coordinates for the shape to be created in an image map', 'Valid list of floating-point numbers. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('crossorigin', {'video', 'audio', 'img', 'script', 'link'}, 'How the element handles crossorigin requests', '"anonymous"; "use-credentials"', {'"use-credentials', 'anonymous'}),
        <class 'tuple'>:('data', {'object'}, 'Address of the resource', 'Valid non-empty URL potentially surrounded by spaces', set()),
        <class 'tuple'>:('datetime', {'ins', 'del'}, 'Date and (optionally) time of the change', 'Valid date string with optional time', set()),
        <class 'tuple'>:('datetime', {'time'}, 'Machine-readable value', 'Valid month string, valid date string, valid yearless date string, valid time string, valid local date and time string, valid time-zone offset string, valid global date and time string, valid week string, valid non-negative integer, or valid duration string', set()),
        <class 'tuple'>:('decoding', {'img'}, 'Decoding hint to use when processing this image for presentation', '"sync"; "async"; "auto"', {'sync', '"async', '"auto'}),
        <class 'tuple'>:('default', {'track'}, 'Enable the track if no other text track is more suitable', 'Boolean attribute', set()),
        <class 'tuple'>:('defer', {'script'}, 'Defer script execution', 'Boolean attribute', set()),
        <class 'tuple'>:('dir', {'HTML'}, 'The text directionality of the element', '"ltr"; "rtl"; "auto"', {'"rtl', 'ltr', '"auto'}),
        <class 'tuple'>:('dir', {'bdo'}, 'The text directionality of the element', '"ltr"; "rtl"', {'"rtl', 'ltr'}),
        <class 'tuple'>:('dirname', {'input', 'textarea'}, "Name of form control to use for sending the element's directionality in form submission", 'Text. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('disabled', {'button', 'select', 'input', 'textarea', 'option', 'optgroup'}, 'Whether the form control is disabled', 'Boolean attribute', set()),
        <class 'tuple'>:('disabled', {'fieldset'}, 'Whether the descendant form controls, except any inside legend, are disabled', 'Boolean attribute', set()),
        <class 'tuple'>:('download', {'area', 'a'}, 'Whether to download the resource instead of navigating to it, and its file name if so', 'Text', set()),
        <class 'tuple'>:('draggable', {'HTML'}, 'Whether the element is draggable', '"true"; "false"', {'"false', 'true'}),
        <class 'tuple'>:('enctype', {'form'}, 'Entry list encoding type to use for form submission', '"application/x-www-form-urlencoded"; "multipart/form-data"; "text/plain"', set()),
        <class 'tuple'>:('enterkeyhint', {'HTML'}, 'Hint for selecting an enter key action', '"enter"; "done"; "go"; "next"; "previous"; "search" "send"', set()),
        <class 'tuple'>:('for', {'label'}, 'Associate the label with form control', 'ID. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('for', {'output'}, 'Specifies controls from which the output was calculated', 'Unordered set of unique space-separated tokens, case-sensitive, consisting of IDs. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('form', {'button', 'fieldset', 'select', 'output', 'input', 'textarea', 'object'}, 'Associates the element with a form element', 'ID. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('formaction', {'input', 'button'}, 'URL to use for form submission', 'Valid non-empty URL potentially surrounded by spaces', set()),
        <class 'tuple'>:('formenctype', {'input', 'button'}, 'Entry list encoding type to use for form submission', '"application/x-www-form-urlencoded"; "multipart/form-data"; "text/plain"', set()),
        <class 'tuple'>:('formmethod', {'input', 'button'}, 'Variant to use for form submission', '"GET"; "POST"; "dialog"', {'"POST', '"dialog', 'GET'}),
        <class 'tuple'>:('formnovalidate', {'input', 'button'}, 'Bypass form control validation for form submission', 'Boolean attribute', set()),
        <class 'tuple'>:('formtarget', {'input', 'button'}, 'Browsing context for form submission', 'Valid browsing context name or keyword', set()),
        <class 'tuple'>:('headers', {'th', 'td'}, 'The header cells for this cell', 'Unordered set of unique space-separated tokens, case-sensitive, consisting of IDs. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('height', {'embed', 'img', 'video', 'canvas', 'iframe', 'input', 'object'}, 'Vertical dimension', 'Valid non-negative integer', set()),
        <class 'tuple'>:('hidden', {'HTML'}, 'Whether the element is relevant', 'Boolean attribute', set()),
        <class 'tuple'>:('high', {'meter'}, 'Low limit of high range', 'Valid floating-point number. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('href', {'area', 'a'}, 'Address of the hyperlink', 'Valid URL potentially surrounded by spaces', set()),
        <class 'tuple'>:('href', {'link'}, 'Address of the hyperlink', 'Valid non-empty URL potentially surrounded by spaces', set()),
        <class 'tuple'>:('href', {'base'}, 'Document base URL', 'Valid URL potentially surrounded by spaces', set()),
        <class 'tuple'>:('hreflang', {'a', 'link'}, 'Language of the linked resource', 'Valid BCP 47 language tag', set()),
        <class 'tuple'>:('http-equiv', {'meta'}, 'Pragma directive', '"content-type"; "default-style"; "refresh"; "x-ua-compatible"; "content-security-policy"', {'content-type', '"default-style', '"refresh', '"x-ua-compatible', '"content-security-policy'}),
        <class 'tuple'>:('id', {'HTML'}, "The element's ID", 'Text. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('imagesizes', {'link'}, 'Image sizes for different page layouts', 'Valid source size list', set()),
        <class 'tuple'>:('imagesrcset', {'link'}, 'Images to use in different situations (e.g., high-resolution displays, small monitors, etc.)', 'Comma-separated list of image candidate strings', set()),
        <class 'tuple'>:('inputmode', {'HTML'}, 'Hint for selecting an input modality', '"none"; "text"; "tel"; "email"; "url"; "numeric"; "decimal"; "search"', {'"numeric', '"email', '"url', 'none', '"text', '"decimal', '"search', '"tel'}),
        <class 'tuple'>:('integrity', {'script', 'link'}, 'Integrity metadata used in Subresource Integrity checks [SRI]', 'Text', set()),
        <class 'tuple'>:('is', {'HTML'}, 'Creates a customized built-in element', 'Valid custom element name of a defined customized built-in element', set()),
        <class 'tuple'>:('ismap', {'img'}, 'Whether the image is a server-side image map', 'Boolean attribute', set()),
        <class 'tuple'>:('itemid', {'HTML'}, 'Global identifier for a microdata item', 'Valid URL potentially surrounded by spaces', set()),
        <class 'tuple'>:('itemprop', {'HTML'}, 'Property names of a microdata item', 'Unordered set of unique space-separated tokens, case-sensitive, consisting of valid absolute URLs, defined property names, or text. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('itemref', {'HTML'}, 'Referenced elements', 'Unordered set of unique space-separated tokens, case-sensitive, consisting of IDs. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('itemscope', {'HTML'}, 'Introduces a microdata item', 'Boolean attribute', set()),
        <class 'tuple'>:('itemtype', {'HTML'}, 'Item types of a microdata item', 'Unordered set of unique space-separated tokens, case-sensitive, consisting of valid absolute URL. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('kind', {'track'}, 'The type of text track', '"subtitles"; "captions"; "descriptions"; "chapters"; "metadata"', {'"captions', '"descriptions', 'subtitles', '"metadata', '"chapters'}),
        <class 'tuple'>:('label', {'track', 'option', 'optgroup'}, 'User-visible label', 'Text', set()),
        <class 'tuple'>:('lang', {'HTML'}, 'Language of the element', 'Valid BCP 47 language tag or the empty string', set()),
        <class 'tuple'>:('list', {'input'}, 'List of autocomplete options', 'ID. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('loop', {'video', 'audio'}, 'Whether to loop the media resource', 'Boolean attribute', set()),
        <class 'tuple'>:('low', {'meter'}, 'High limit of low range', 'Valid floating-point number. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('manifest', {'html'}, 'Application cache manifest', 'Valid non-empty URL potentially surrounded by spaces', set()),
        <class 'tuple'>:('max', {'input'}, 'Maximum value', 'Varies. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('max', {'meter', 'progress'}, 'Upper bound of range', 'Valid floating-point number. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('maxlength', {'input', 'textarea'}, 'Maximum length of value', 'Valid non-negative integer', set()),
        <class 'tuple'>:('media', {'source', 'link', 'style'}, 'Applicable media', 'Valid media query list', set()),
        <class 'tuple'>:('method', {'form'}, 'Variant to use for form submission', '"GET"; "POST"; "dialog"', {'"POST', '"dialog', 'GET'}),
        <class 'tuple'>:('min', {'input'}, 'Minimum value', 'Varies. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('min', {'meter'}, 'Lower bound of range', 'Valid floating-point number. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('minlength', {'input', 'textarea'}, 'Minimum length of value', 'Valid non-negative integer', set()),
        <class 'tuple'>:('multiple', {'select', 'input'}, 'Whether to allow multiple values', 'Boolean attribute', set()),
        <class 'tuple'>:('muted', {'video', 'audio'}, 'Whether to mute the media resource by default', 'Boolean attribute', set()),
        <class 'tuple'>:('name', {'button', 'fieldset', 'select', 'output', 'input', 'textarea'}, 'Name of the element to use for form submission and in the form.elements API', 'Text. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('name', {'form'}, 'Name of form to use in the document.forms API', 'Text. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('name', {'iframe', 'object'}, 'Name of nested browsing context', 'Valid browsing context name or keyword', set()),
        <class 'tuple'>:('name', {'map'}, 'Name of image map to reference from the usemap attribute', 'Text. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('name', {'meta'}, 'Metadata name', 'Text. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('name', {'param'}, 'Name of parameter', 'Text', set()),
        <class 'tuple'>:('name', {'slot'}, 'Name of shadow tree slot', 'Text', set()),
        <class 'tuple'>:('nomodule', {'script'}, 'Prevents execution in user agents that support module scripts', 'Boolean attribute', set()),
        <class 'tuple'>:('nonce', {'HTML'}, 'Cryptographic nonce used in Content Security Policy checks [CSP]', 'Text', set()),
        <class 'tuple'>:('novalidate', {'form'}, 'Bypass form control validation for form submission', 'Boolean attribute', set()),
        <class 'tuple'>:('open', {'details'}, 'Whether the details are visible', 'Boolean attribute', set()),
        <class 'tuple'>:('open', {'dialog'}, 'Whether the dialog box is showing', 'Boolean attribute', set()),
        <class 'tuple'>:('optimum', {'meter'}, 'Optimum value in gauge', 'Valid floating-point number. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('pattern', {'input'}, "Pattern to be matched by the form control's value", 'Regular expression matching the JavaScript Pattern production', set()),
        <class 'tuple'>:('ping', {'area', 'a'}, 'URLs to ping', 'Set of space-separated tokens consisting of valid non-empty URLs', set()),
        <class 'tuple'>:('placeholder', {'input', 'textarea'}, 'User-visible label to be placed within the form control', 'Text. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('playsinline', {'video'}, "Encourage the user agent to display video content within the element's playback area", 'Boolean attribute', set()),
        <class 'tuple'>:('poster', {'video'}, 'Poster frame to show prior to video playback', 'Valid non-empty URL potentially surrounded by spaces', set()),
        <class 'tuple'>:('preload', {'video', 'audio'}, 'Hints how much buffering the media resource will likely need', '"none"; "metadata"; "auto"', {'"metadata', '"auto', 'none'}),
        <class 'tuple'>:('readonly', {'input', 'textarea'}, 'Whether to allow the value to be edited by the user', 'Boolean attribute', set()),
        <class 'tuple'>:('referrerpolicy', {'area', 'a', 'img', 'script', 'link', 'iframe'}, 'Referrer policy for fetches initiated by the element', 'Referrer policy', set()),
        <class 'tuple'>:('rel', {'area', 'a'}, 'Relationship between the location in the document containing the hyperlink and the destination resource', 'Unordered set of unique space-separated tokens. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('rel', {'link'}, 'Relationship between the document containing the hyperlink and the destination resource', 'Unordered set of unique space-separated tokens. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('required', {'select', 'input', 'textarea'}, 'Whether the control is required for form submission', 'Boolean attribute', set()),
        <class 'tuple'>:('reversed', {'ol'}, 'Number the list backwards', 'Boolean attribute', set()),
        <class 'tuple'>:('rows', {'textarea'}, 'Number of lines to show', 'Valid non-negative integer greater than zero', set()),
        <class 'tuple'>:('rowspan', {'th', 'td'}, 'Number of rows that the cell is to span', 'Valid non-negative integer', set()),
        <class 'tuple'>:('sandbox', {'iframe'}, 'Security rules for nested content', 'Unordered set of unique space-separated tokens, ASCII case-insensitive, consisting of "allow-forms", "allow-modals", "allow-orientation-lock", "allow-pointer-lock", "allow-popups", "allow-popups-to-escape-sandbox", "allow-presentation", "allow-same-origin", "allow-scripts" and "allow-top-navigation"', set()),
        <class 'tuple'>:('scope', {'th'}, 'Specifies which cells the header cell applies to', '"row"; "col"; "rowgroup"; "colgroup"', {'row', '"rowgroup', '"col', '"colgroup'}),
        <class 'tuple'>:('selected', {'option'}, 'Whether the option is selected by default', 'Boolean attribute', set()),
        <class 'tuple'>:('shape', {'area'}, 'The kind of shape to be created in an image map', '"circle"; "default"; "poly"; "rect"', {'circle', '"default', '"poly', '"rect'}),
        <class 'tuple'>:('size', {'select', 'input'}, 'Size of the control', 'Valid non-negative integer greater than zero', set()),
        <class 'tuple'>:('sizes', {'link'}, 'Sizes of the icons (for rel="icon")', 'Unordered set of unique space-separated tokens, ASCII case-insensitive, consisting of sizes. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('sizes', {'img', 'source'}, 'Image sizes for different page layouts', 'Valid source size list', set()),
        <class 'tuple'>:('slot', {'HTML'}, "The element's desired slot", 'Text', set()),
        <class 'tuple'>:('span', {'colgroup', 'col'}, 'Number of columns spanned by the element', 'Valid non-negative integer greater than zero', set()),
        <class 'tuple'>:('spellcheck', {'HTML'}, 'Whether the element is to have its spelling and grammar checked', '"true"; "false"', {'"false', 'true'}),
        <class 'tuple'>:('src', {'track', 'embed', 'audio', 'img', 'script', 'source', 'video', 'iframe', 'input'}, 'Address of the resource', 'Valid non-empty URL potentially surrounded by spaces', set()),
        <class 'tuple'>:('srcdoc', {'iframe'}, 'A document to render in the iframe', 'The source of an iframe srcdoc document. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('srclang', {'track'}, 'Language of the text track', 'Valid BCP 47 language tag', set()),
        <class 'tuple'>:('srcset', {'img', 'source'}, 'Images to use in different situations (e.g., high-resolution displays, small monitors, etc.)', 'Comma-separated list of image candidate strings', set()),
        <class 'tuple'>:('start', {'ol'}, 'Starting value of the list', 'Valid integer', set()),
        <class 'tuple'>:('step', {'input'}, "Granularity to be matched by the form control's value", 'Valid floating-point number greater than zero, or "any"', set()),
        <class 'tuple'>:('style', {'HTML'}, 'Presentational and formatting instructions', 'CSS declarations. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('tabindex', {'HTML'}, 'Whether the element is focusable, and the relative order of the element for the purposes of sequential focus navigation', 'Valid integer', set()),
        <class 'tuple'>:('target', {'area', 'a'}, 'Browsing context for hyperlink navigation', 'Valid browsing context name or keyword', set()),
        <class 'tuple'>:('target', {'base'}, 'Default browsing context for hyperlink navigation and form submission', 'Valid browsing context name or keyword', set()),
        <class 'tuple'>:('target', {'form'}, 'Browsing context for form submission', 'Valid browsing context name or keyword', set()),
        <class 'tuple'>:('title', {'HTML'}, 'Advisory information for the element', 'Text', set()),
        <class 'tuple'>:('title', {'abbr', 'dfn'}, 'Full term or expansion of abbreviation', 'Text', set()),
        <class 'tuple'>:('title', {'input'}, 'Description of pattern (when used with pattern attribute)', 'Text', set()),
        <class 'tuple'>:('title', {'link'}, 'Title of the link', 'Text', set()),
        <class 'tuple'>:('title', {'link', 'style'}, 'CSS style sheet set name', 'Text', set()),
        <class 'tuple'>:('translate', {'HTML'}, 'Whether the element is to be translated when the page is localized', '"yes"; "no"', {'yes', '"no'}),
        <class 'tuple'>:('type', {'a', 'link'}, 'Hint for the type of the referenced resource', 'Valid MIME type string', set()),
        <class 'tuple'>:('type', {'button'}, 'Type of button', '"submit"; "reset"; "button"', {'submit', '"reset', '"button'}),
        <class 'tuple'>:('type', {'source', 'object', 'embed'}, 'Type of embedded resource', 'Valid MIME type string', set()),
        <class 'tuple'>:('type', {'input'}, 'Type of form control', 'input type keyword', set()),
        <class 'tuple'>:('type', {'ol'}, 'Kind of list marker', '"1"; "a"; "A"; "i"; "I"', {'"I', '"A', '1', '"a', '"i'}),
        <class 'tuple'>:('type', {'script'}, 'Type of script', '"module"; a valid MIME type string that is not a JavaScript MIME type essence match', set()),
        <class 'tuple'>:('typemustmatch', {'object'}, 'Whether the type attribute and the Content-Type value need to match for the resource to be used', 'Boolean attribute', set()),
        <class 'tuple'>:('usemap', {'img', 'object'}, 'Name of image map to use', 'Valid hash-name reference. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('value', {'button', 'option'}, 'Value to be used for form submission', 'Text', set()),
        <class 'tuple'>:('value', {'data'}, 'Machine-readable value', 'Text. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('value', {'input'}, 'Value of the form control', 'Varies. The actual rules are more complicated than indicated.', set()),
        <class 'tuple'>:('value', {'li'}, 'Ordinal value of the list item', 'Valid integer', set()),
        <class 'tuple'>:('value', {'meter', 'progress'}, 'Current value of the element', 'Valid floating-point number', set()),
        <class 'tuple'>:('value', {'param'}, 'Value of parameter', 'Text', set()),
        <class 'tuple'>:('width', {'embed', 'img', 'video', 'canvas', 'iframe', 'input', 'object'}, 'Horizontal dimension', 'Valid non-negative integer', set()),
        <class 'tuple'>:('wrap', {'textarea'}, 'How the value of the form control is to be wrapped for form submission', '"soft"; "hard"', {'soft', '"hard'})
    ],
    'categories':
    [
        <class 'tuple'>:('Autocapitalize-inheriting elements', {'button', 'fieldset', 'select', 'output', 'input', 'textarea'}, '—'),
        <class 'tuple'>:('Embedded content', {'embed', 'picture', 'audio', 'img', 'svg', 'math', 'canvas', 'iframe', 'video', 'object'}, '—'),
        <class 'tuple'>:('Flow content', {'h4', 'dialog', 'ins', 'a', 'var', 'picture', 'audio', 'time', 'strong', 'header', 'footer', 'video', 'canvas', 'dfn', 'div', 'input', 'p', 'sup', 'textarea', 'wbr', 'abbr', 'ruby', 'template', 'nav', 'h2', 'map', 'meter', 'form', 'sub', 'h3', 'ol', 'img', 'cite', 'output', 'slot', 'menu', 'small', 'i', 'del', 'progress', 's', 'h1', 'samp', 'q', 'section', 'Text', 'b', 'h5', 'script', 'table', 'kbd', 'figure', 'math', 'hr', 'iframe', 'address', 'bdi', 'br', 'bdo', 'data', 'pre', 'ul', 'object', 'article', 'em', 'hgroup', 'button', 'embed', 'fieldset', 'label', 'select', 'svg', 'u', 'datalist', 'span', 'h6', 'blockquote', 'mark', 'aside', 'code', 'noscript', 'details', 'dl'}, 'area (if it is a descendant of a map element); link (if it is allowed in the body); main (if it is a hierarchically correct main element); meta (if the itemprop attribute is present)'),
        <class 'tuple'>:('Form-associated elements', {'button', 'fieldset', 'label', 'select', 'output', 'img', 'input', 'textarea', 'object'}, '—'),
        <class 'tuple'>:('Heading content', {'h4', 'h2', 'h1', 'hgroup', 'h3', 'h5', 'h6'}, '—'),
        <class 'tuple'>:('Interactive content', {'button', 'embed', 'label', 'select', 'iframe', 'textarea', 'details'}, 'a (if the href attribute is present); audio (if the controls attribute is present); img (if the usemap attribute is present); input (if the type attribute is not in the Hidden state); object (if the usemap attribute is present); video (if the controls attribute is present); The tabindex attribute can also make any element into interactive content.'),
        <class 'tuple'>:('Labelable elements', {'meter', 'button', 'select', 'output', 'input', 'textarea', 'progress'}, '—'),
        <class 'tuple'>:('Listed elements', {'button', 'fieldset', 'select', 'output', 'input', 'textarea', 'object'}, '—'),
        <class 'tuple'>:('Metadata content', {'base', 'style', 'meta', 'title', 'script', 'link', 'noscript', 'template'}, '—'),
        <class 'tuple'>:('Palpable content', {'h4', 'ins', 'var', 'a', 'time', 'strong', 'header', 'footer', 'video', 'canvas', 'dfn', 'div', 'p', 'sup', 'textarea', 'abbr', 'ruby', 'nav', 'h2', 'map', 'meter', 'form', 'sub', 'h3', 'img', 'cite', 'output', 'small', 'i', 'progress', 's', 'h1', 'samp', 'q', 'section', 'b', 'h5', 'table', 'kbd', 'figure', 'math', 'iframe', 'pre', 'address', 'bdi', 'bdo', 'data', 'object', 'article', 'em', 'hgroup', 'button', 'embed', 'fieldset', 'label', 'select', 'svg', 'u', 'span', 'h6', 'blockquote', 'mark', 'aside', 'code', 'details', 'main'}, "audio (if the controls attribute is present); dl (if the element's children include at least one name-value group); input (if the type attribute is not in the Hidden state); menu (if the element's children include at least one li element); ol (if the element's children include at least one li element); ul (if the element's children include at least one li element); Text that is not inter-element whitespace"),
        <class 'tuple'>:('Phrasing content', {'ins', 'var', 'a', 'picture', 'audio', 'time', 'strong', 'video', 'canvas', 'dfn', 'input', 'sup', 'textarea', 'wbr', 'abbr', 'ruby', 'template', 'map', 'meter', 'sub', 'img', 'cite', 'output', 'slot', 'small', 'i', 'del', 'progress', 's', 'samp', 'q', 'b', 'script', 'kbd', 'math', 'iframe', 'Text', 'bdi', 'br', 'bdo', 'data', 'object', 'em', 'button', 'embed', 'label', 'select', 'svg', 'u', 'datalist', 'span', 'mark', 'code', 'noscript'}, 'area (if it is a descendant of a  map element); link (if it is allowed in the body); meta (if the itemprop attribute is present)'),
        <class 'tuple'>:('Resettable elements', {'select', 'input', 'output', 'textarea'}, '—'),
        <class 'tuple'>:('Script-supporting elements', {'template', 'script'}, '—'),
        <class 'tuple'>:('Sectioning content', {'aside', 'article', 'nav', 'section'}, '—'),
        <class 'tuple'>:('Sectioning roots', {'dialog', 'fieldset', 'body', 'td', 'figure', 'blockquote', 'details'}, '—'),
        <class 'tuple'>:('Submittable elements', {'select', 'input', 'object', 'textarea', 'button'}, '—')
    ],
    'elements':
    [
        <class 'tuple'>:('a', 'Hyperlink', {'flow', 'phrasing', 'interactive', 'palpable'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'ping', 'itemid', 'href', 'hreflang', 'referrerpolicy', 'spellcheck', 'draggable', 'itemscope', 'style', 'title', 'target', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'download', 'lang', 'type', 'rel', 'dir', 'itemref', 'tabindex', 'nonce', 'autocapitalize'}, {'transparent'}),
        <class 'tuple'>:('abbr', 'Abbreviation', {'flow', 'phrasing', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('address', 'Contact information for a page or article element', {'flow', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'flow'}),
        <class 'tuple'>:('area', 'Hyperlink or dead area on an image map', {'flow', 'phrasing'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'ping', 'itemid', 'href', 'referrerpolicy', 'spellcheck', 'draggable', 'itemscope', 'style', 'title', 'coords', 'target', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'download', 'lang', 'shape', 'rel', 'dir', 'itemref', 'tabindex', 'alt', 'nonce', 'autocapitalize'}, {'empty'}),
        <class 'tuple'>:('article', 'Self-contained syndicatable or reusable composition', {'flow', 'palpable', 'sectioning'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'flow'}),
        <class 'tuple'>:('aside', 'Sidebar for tangentially related content', {'flow', 'palpable', 'sectioning'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'flow'}),
        <class 'tuple'>:('audio', 'Audio player', {'flow', 'phrasing', 'interactive', 'embedded', 'palpable'}, {'accesskey', 'src', 'hidden', 'autoplay', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'draggable', 'itemscope', 'muted', 'style', 'title', 'enterkeyhint', 'translate', 'crossorigin', 'contenteditable', 'is', 'inputmode', 'controls', 'loop', 'lang', 'dir', 'itemref', 'tabindex', 'preload', 'nonce', 'autocapitalize'}, {'source', 'track', 'transparent'}),
        <class 'tuple'>:('b', 'Keywords', {'flow', 'phrasing', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('base', 'Base URL and default target browsing context for hyperlinks and forms', {'metadata'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'href', 'spellcheck', 'draggable', 'itemscope', 'style', 'title', 'target', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'dir', 'itemref', 'tabindex', 'nonce', 'autocapitalize'}, {'empty'}),
        <class 'tuple'>:('bdi', 'Text directionality isolation', {'flow', 'phrasing', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('bdo', 'Text directionality formatting', {'flow', 'phrasing', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('blockquote', 'A section quoted from another source', {'flow', 'palpable', 'sectioning root'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'draggable', 'itemscope', 'style', 'title', 'cite', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'dir', 'itemref', 'tabindex', 'nonce', 'autocapitalize'}, {'flow'}),
        <class 'tuple'>:('body', 'Document body', {'sectioning root'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'onoffline', 'onunhandledrejection', 'onrejectionhandled', 'ononline', 'spellcheck', 'draggable', 'itemscope', 'style', 'title', 'onpageshow', 'onmessageerror', 'onpopstate', 'enterkeyhint', 'translate', 'contenteditable', 'onunload', 'is', 'onmessage', 'inputmode', 'lang', 'onafterprint', 'onlanguagechange', 'onhashchange', 'dir', 'itemref', 'onbeforeprint', 'onstorage', 'tabindex', 'onbeforeunload', 'nonce', 'autocapitalize', 'onpagehide'}, {'flow'}),
        <class 'tuple'>:('br', 'Line break, e.g. in poem or postal address', {'flow', 'phrasing'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'empty'}),
        <class 'tuple'>:('button', 'Button control', {'listed', 'form-associated', 'flow', 'palpable', 'submittable', 'interactive', 'labelable', 'phrasing'}, {'accesskey', 'formnovalidate', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'value', 'draggable', 'itemscope', 'form', 'style', 'autofocus', 'title', 'name', 'enterkeyhint', 'translate', 'formenctype', 'contenteditable', 'is', 'inputmode', 'lang', 'disabled', 'formaction', 'type', 'dir', 'itemref', 'tabindex', 'formmethod', 'nonce', 'autocapitalize', 'formtarget'}, {'phrasing'}),
        <class 'tuple'>:('canvas', 'Scriptable bitmap canvas', {'flow', 'phrasing', 'palpable', 'embedded'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'draggable', 'itemscope', 'style', 'title', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'width', 'dir', 'itemref', 'tabindex', 'height', 'nonce', 'autocapitalize'}, {'transparent'}),
        <class 'tuple'>:('caption', 'Table caption', {'none'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'flow'}),
        <class 'tuple'>:('cite', 'Title of a work', {'flow', 'phrasing', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('code', 'Computer code', {'flow', 'phrasing', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('col', 'Table column', {'none'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'draggable', 'itemscope', 'style', 'title', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'dir', 'itemref', 'span', 'tabindex', 'nonce', 'autocapitalize'}, {'empty'}),
        <class 'tuple'>:('colgroup', 'Group of columns in a table', {'none'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'draggable', 'itemscope', 'style', 'title', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'dir', 'itemref', 'span', 'tabindex', 'nonce', 'autocapitalize'}, {'template', 'col'}),
        <class 'tuple'>:('data', 'Machine-readable equivalent', {'flow', 'phrasing', 'palpable'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'value', 'draggable', 'itemscope', 'style', 'title', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'dir', 'itemref', 'tabindex', 'nonce', 'autocapitalize'}, {'phrasing'}),
        <class 'tuple'>:('datalist', 'Container for options for combo box control', {'flow', 'phrasing'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing', 'script-supporting elements', 'option'}),
        <class 'tuple'>:('dd', 'Content for corresponding dt element(s)', {'none'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'flow'}),
        <class 'tuple'>:('del', 'A removal from the document', {'flow', 'phrasing'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'draggable', 'itemscope', 'style', 'title', 'cite', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'datetime', 'dir', 'itemref', 'tabindex', 'nonce', 'autocapitalize'}, {'transparent'}),
        <class 'tuple'>:('details', 'Disclosure control for hiding details', {'flow', 'interactive', 'palpable', 'sectioning root'}, {'accesskey', 'open', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'draggable', 'itemscope', 'style', 'title', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'dir', 'itemref', 'tabindex', 'nonce', 'autocapitalize'}, {'flow', 'summary'}),
        <class 'tuple'>:('dfn', 'Defining instance', {'flow', 'phrasing', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('dialog', 'Dialog box or window', {'flow', 'sectioning root'}, {'accesskey', 'open', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'draggable', 'itemscope', 'style', 'title', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'dir', 'itemref', 'tabindex', 'nonce', 'autocapitalize'}, {'flow'}),
        <class 'tuple'>:('div', 'Generic flow container, or container for name-value groups in dl elements', {'flow', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'flow'}),
        <class 'tuple'>:('dl', 'Association list consisting of zero or more name-value groups', {'flow', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'script-supporting elements', 'div', 'dt', 'dd'}),
        <class 'tuple'>:('dt', 'Legend for corresponding dd element(s)', {'none'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'flow'}),
        <class 'tuple'>:('em', 'Stress emphasis', {'flow', 'phrasing', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('embed', 'Plugin', {'flow', 'phrasing', 'interactive', 'embedded', 'palpable'}, {'accesskey', 'src', 'any*', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'draggable', 'itemscope', 'style', 'title', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'width', 'type', 'dir', 'itemref', 'tabindex', 'height', 'nonce', 'autocapitalize'}, {'empty'}),
        <class 'tuple'>:('fieldset', 'Group of form controls', {'listed', 'form-associated', 'flow', 'palpable', 'sectioning root'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'draggable', 'itemscope', 'form', 'style', 'title', 'name', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'disabled', 'dir', 'itemref', 'tabindex', 'nonce', 'autocapitalize'}, {'flow', 'legend'}),
        <class 'tuple'>:('figcaption', 'Caption for figure', {'none'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'flow'}),
        <class 'tuple'>:('figure', 'Figure with optional caption', {'flow', 'palpable', 'sectioning root'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'figcaption', 'flow'}),
        <class 'tuple'>:('footer', 'Footer for a page or section', {'flow', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'flow'}),
        <class 'tuple'>:('form', 'User-submittable form', {'flow', 'palpable'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'method', 'itemid', 'spellcheck', 'draggable', 'autocomplete', 'itemscope', 'style', 'title', 'enctype', 'accept-charset', 'name', 'target', 'enterkeyhint', 'translate', 'contenteditable', 'action', 'is', 'novalidate', 'inputmode', 'lang', 'dir', 'itemref', 'tabindex', 'nonce', 'autocapitalize'}, {'flow'}),
        <class 'tuple'>:('h1', 'Section heading', {'flow', 'heading', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('h2', 'Section heading', {'flow', 'heading', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('h3', 'Section heading', {'flow', 'heading', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('h4', 'Section heading', {'flow', 'heading', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('h5', 'Section heading', {'flow', 'heading', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('h6', 'Section heading', {'flow', 'heading', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('head', 'Container for document metadata', {'none'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'metadata content'}),
        <class 'tuple'>:('header', 'Introductory or navigational aids for a page or section', {'flow', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'flow'}),
        <class 'tuple'>:('hgroup', 'heading group', {'flow', 'heading', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'h4', 'h2', 'h1', 'script-supporting elements', 'h3', 'h5', 'h6'}),
        <class 'tuple'>:('hr', 'Thematic break', {'flow'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'empty'}),
        <class 'tuple'>:('html', 'Root element', {'none'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'draggable', 'manifest', 'itemscope', 'style', 'title', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'dir', 'itemref', 'tabindex', 'nonce', 'autocapitalize'}, {'body', 'head'}),
        <class 'tuple'>:('i', 'Alternate voice', {'flow', 'phrasing', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('iframe', 'Nested browsing context', {'flow', 'phrasing', 'interactive', 'embedded', 'palpable'}, {'accesskey', 'src', 'sandbox', 'hidden', 'itemprop', 'itemtype', 'itemid', 'referrerpolicy', 'spellcheck', 'draggable', 'allowpaymentrequest', 'itemscope', 'style', 'allowfullscreen', 'title', 'name', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'width', 'dir', 'itemref', 'tabindex', 'allow', 'srcdoc', 'height', 'nonce', 'autocapitalize'}, {'empty'}),
        <class 'tuple'>:('img', 'Image', {'form-associated', 'flow', 'palpable', 'interactive', 'embedded', 'phrasing'}, {'accesskey', 'src', 'hidden', 'itemprop', 'itemtype', 'itemid', 'referrerpolicy', 'usemap', 'spellcheck', 'draggable', 'itemscope', 'style', 'title', 'decoding', 'enterkeyhint', 'translate', 'crossorigin', 'contenteditable', 'is', 'inputmode', 'lang', 'width', 'srcset', 'dir', 'itemref', 'tabindex', 'ismap', 'height', 'alt', 'nonce', 'autocapitalize'}, {'empty'}),
        <class 'tuple'>:('input', 'Form control', {'listed', 'form-associated', 'flow', 'palpable', 'submittable', 'resettable', 'interactive', 'labelable', 'phrasing'}, {'pattern', 'accesskey', 'checked', 'placeholder', 'formnovalidate', 'src', 'hidden', 'itemprop', 'itemtype', 'itemid', 'multiple', 'dirname', 'spellcheck', 'value', 'step', 'draggable', 'autocomplete', 'min', 'itemscope', 'list', 'form', 'style', 'autofocus', 'title', 'name', 'enterkeyhint', 'translate', 'formenctype', 'contenteditable', 'readonly', 'is', 'inputmode', 'maxlength', 'minlength', 'lang', 'disabled', 'formaction', 'width', 'type', 'accept', 'size', 'dir', 'itemref', 'required', 'tabindex', 'height', 'formmethod', 'max', 'alt', 'nonce', 'autocapitalize', 'formtarget'}, {'empty'}),
        <class 'tuple'>:('ins', 'An addition to the document', {'flow', 'phrasing', 'palpable'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'draggable', 'itemscope', 'style', 'title', 'cite', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'datetime', 'dir', 'itemref', 'tabindex', 'nonce', 'autocapitalize'}, {'transparent'}),
        <class 'tuple'>:('kbd', 'User input', {'flow', 'phrasing', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('label', 'Caption for a form control', {'flow', 'phrasing', 'interactive', 'palpable'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'draggable', 'itemscope', 'style', 'title', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'for', 'lang', 'dir', 'itemref', 'tabindex', 'nonce', 'autocapitalize'}, {'phrasing'}),
        <class 'tuple'>:('legend', 'Caption for fieldset', {'none'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('li', 'List item', {'none'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'draggable', 'itemscope', 'style', 'title', 'value*', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'dir', 'itemref', 'tabindex', 'nonce', 'autocapitalize'}, {'flow'}),
        <class 'tuple'>:('link', 'Link metadata', {'flow', 'phrasing', 'metadata'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'hreflang', 'itemid', 'href', 'referrerpolicy', 'spellcheck', 'media', 'draggable', 'itemscope', 'style', 'integrity', 'title', 'enterkeyhint', 'as', 'translate', 'crossorigin', 'contenteditable', 'is', 'inputmode', 'lang', 'imagesrcset', 'type', 'rel', 'dir', 'itemref', 'imagesizes', 'tabindex', 'sizes', 'nonce', 'autocapitalize'}, {'empty'}),
        <class 'tuple'>:('main', 'Container for the dominant contents of the document', {'flow', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'flow'}),
        <class 'tuple'>:('map', 'Image map', {'flow', 'phrasing', 'palpable'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'draggable', 'itemscope', 'style', 'title', 'name', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'dir', 'itemref', 'tabindex', 'nonce', 'autocapitalize'}, {'area', 'transparent'}),
        <class 'tuple'>:('mark', 'Highlight', {'flow', 'phrasing', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('math', 'MathML root', {'flow', 'phrasing', 'palpable', 'embedded'}, {'per [MATHML]'}, {'per [MATHML]'}),
        <class 'tuple'>:('menu', 'Menu of commands', {'flow', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'li', 'script-supporting elements'}),
        <class 'tuple'>:('meta', 'Text metadata', {'flow', 'phrasing', 'metadata'}, {'accesskey', 'content', 'http-equiv', 'hidden', 'itemprop', 'itemtype', 'itemid', 'charset', 'spellcheck', 'draggable', 'itemscope', 'style', 'title', 'name', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'dir', 'itemref', 'tabindex', 'nonce', 'autocapitalize'}, {'empty'}),
        <class 'tuple'>:('meter', 'Gauge', {'flow', 'phrasing', 'palpable', 'labelable'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'high', 'low', 'spellcheck', 'value', 'draggable', 'min', 'optimum', 'itemscope', 'style', 'title', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'dir', 'itemref', 'tabindex', 'max', 'nonce', 'autocapitalize'}, {'phrasing'}),
        <class 'tuple'>:('nav', 'Section with navigational links', {'flow', 'palpable', 'sectioning'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'flow'}),
        <class 'tuple'>:('noscript', 'Fallback content for script', {'flow', 'phrasing', 'metadata'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'varies'}),
        <class 'tuple'>:('object', 'Image, nested browsing context, or plugin', {'listed', 'form-associated', 'flow', 'palpable', 'submittable', 'interactive', 'embedded', 'phrasing'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'usemap', 'spellcheck', 'draggable', 'itemscope', 'form', 'style', 'title', 'name', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'width', 'data', 'type', 'typemustmatch', 'dir', 'itemref', 'tabindex', 'height', 'nonce', 'autocapitalize'}, {'param', 'transparent'}),
        <class 'tuple'>:('ol', 'Ordered list', {'flow', 'palpable'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'draggable', 'itemscope', 'style', 'title', 'start', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'type', 'dir', 'itemref', 'tabindex', 'reversed', 'nonce', 'autocapitalize'}, {'li', 'script-supporting elements'}),
        <class 'tuple'>:('optgroup', 'Group of options in a list box', {'none'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'draggable', 'itemscope', 'style', 'title', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'disabled', 'dir', 'itemref', 'label', 'tabindex', 'nonce', 'autocapitalize'}, {'script-supporting elements', 'option'}),
        <class 'tuple'>:('option', 'Option in a list box or combo box control', {'none'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'value', 'draggable', 'itemscope', 'selected', 'style', 'title', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'disabled', 'dir', 'itemref', 'label', 'tabindex', 'nonce', 'autocapitalize'}, {'text'}),
        <class 'tuple'>:('output', 'Calculated output value', {'listed', 'form-associated', 'flow', 'palpable', 'resettable', 'labelable', 'phrasing'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'draggable', 'itemscope', 'form', 'style', 'title', 'name', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'for', 'lang', 'dir', 'itemref', 'tabindex', 'nonce', 'autocapitalize'}, {'phrasing'}),
        <class 'tuple'>:('p', 'Paragraph', {'flow', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('param', 'Parameter for object', {'none'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'value', 'draggable', 'itemscope', 'style', 'title', 'name', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'dir', 'itemref', 'tabindex', 'nonce', 'autocapitalize'}, {'empty'}),
        <class 'tuple'>:('picture', 'Image', {'flow', 'phrasing', 'embedded'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'source', 'script-supporting elements', 'one img'}),
        <class 'tuple'>:('pre', 'Block of preformatted text', {'flow', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('progress', 'Progress bar', {'flow', 'phrasing', 'palpable', 'labelable'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'value', 'draggable', 'itemscope', 'style', 'title', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'dir', 'itemref', 'tabindex', 'max', 'nonce', 'autocapitalize'}, {'phrasing'}),
        <class 'tuple'>:('q', 'Quotation', {'flow', 'phrasing', 'palpable'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'draggable', 'itemscope', 'style', 'title', 'cite', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'dir', 'itemref', 'tabindex', 'nonce', 'autocapitalize'}, {'phrasing'}),
        <class 'tuple'>:('rp', 'Parenthesis for ruby annotation text', {'none'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'text'}),
        <class 'tuple'>:('rt', 'Ruby annotation text', {'none'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('ruby', 'Ruby annotation(s)', {'flow', 'phrasing', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'rt', 'rp', 'phrasing'}),
        <class 'tuple'>:('s', 'Inaccurate text', {'flow', 'phrasing', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('samp', 'Computer output', {'flow', 'phrasing', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('script', 'Embedded script', {'script-supporting', 'flow', 'phrasing', 'metadata'}, {'accesskey', 'src', 'hidden', 'itemprop', 'itemtype', 'itemid', 'referrerpolicy', 'spellcheck', 'draggable', 'itemscope', 'style', 'integrity', 'title', 'enterkeyhint', 'translate', 'crossorigin', 'contenteditable', 'is', 'inputmode', 'defer', 'lang', 'async', 'type', 'dir', 'itemref', 'tabindex', 'nonce', 'autocapitalize'}, {'script, data, or script documentation'}),
        <class 'tuple'>:('section', 'Generic document or application section', {'flow', 'palpable', 'sectioning'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'flow'}),
        <class 'tuple'>:('select', 'List box control', {'listed', 'form-associated', 'flow', 'palpable', 'submittable', 'resettable', 'interactive', 'labelable', 'phrasing'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'multiple', 'spellcheck', 'draggable', 'autocomplete', 'itemscope', 'form', 'style', 'autofocus', 'title', 'name', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'disabled', 'size', 'dir', 'itemref', 'required', 'tabindex', 'nonce', 'autocapitalize'}, {'script-supporting elements', 'option', 'optgroup'}),
        <class 'tuple'>:('slot', 'Shadow tree slot', {'flow', 'phrasing'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'draggable', 'itemscope', 'style', 'title', 'name', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'dir', 'itemref', 'tabindex', 'nonce', 'autocapitalize'}, {'transparent'}),
        <class 'tuple'>:('small', 'Side comment', {'flow', 'phrasing', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('source', 'Image source for img or media source for video or audio', {'none'}, {'accesskey', 'src', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'media', 'draggable', 'itemscope', 'style', 'title', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'type', 'srcset', 'dir', 'itemref', 'tabindex', 'sizes', 'nonce', 'autocapitalize'}, {'empty'}),
        <class 'tuple'>:('span', 'Generic phrasing container', {'flow', 'phrasing', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('strong', 'Importance', {'flow', 'phrasing', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('style', 'Embedded styling information', {'metadata'}, {'', 'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'media', 'draggable', 'itemscope', 'style', 'title', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'dir', 'itemref', 'tabindex', 'nonce', 'autocapitalize'}, {'text'}),
        <class 'tuple'>:('sub', 'Subscript', {'flow', 'phrasing', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('summary', 'Caption for details', {'none'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('sup', 'Superscript', {'flow', 'phrasing', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('svg', 'SVG root', {'flow', 'phrasing', 'palpable', 'embedded'}, {'per [SVG]'}, {'per [SVG]'}),
        <class 'tuple'>:('table', 'Table', {'flow', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'caption', 'colgroup', 'script-supporting elements', 'tbody', 'tr', 'thead', 'tfoot'}),
        <class 'tuple'>:('tbody', 'Group of rows in a table', {'none'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'tr', 'script-supporting elements'}),
        <class 'tuple'>:('td', 'Table cell', {'sectioning root'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'draggable', 'rowspan', 'itemscope', 'style', 'title', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'dir', 'itemref', 'tabindex', 'colspan', 'headers', 'nonce', 'autocapitalize'}, {'flow'}),
        <class 'tuple'>:('template', 'Template', {'script-supporting', 'flow', 'phrasing', 'metadata'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'empty'}),
        <class 'tuple'>:('textarea', 'Multiline text controls', {'listed', 'form-associated', 'flow', 'palpable', 'submittable', 'resettable', 'interactive', 'labelable', 'phrasing'}, {'placeholder', 'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'dirname', 'spellcheck', 'draggable', 'itemscope', 'form', 'style', 'autofocus', 'title', 'name', 'enterkeyhint', 'rows', 'translate', 'contenteditable', 'readonly', 'is', 'inputmode', 'maxlength', 'minlength', 'lang', 'wrap', 'disabled', 'dir', 'itemref', 'cols', 'required', 'tabindex', 'nonce', 'autocapitalize'}, {'text'}),
        <class 'tuple'>:('tfoot', 'Group of footer rows in a table', {'none'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'tr', 'script-supporting elements'}),
        <class 'tuple'>:('th', 'Table header cell', {'interactive'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'abbr', 'draggable', 'rowspan', 'itemscope', 'style', 'title', 'scope', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'dir', 'itemref', 'tabindex', 'colspan', 'headers', 'nonce', 'autocapitalize'}, {'flow'}),
        <class 'tuple'>:('thead', 'Group of heading rows in a table', {'none'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'tr', 'script-supporting elements'}),
        <class 'tuple'>:('time', 'Machine-readable equivalent of date- or time-related data', {'flow', 'phrasing', 'palpable'}, {'accesskey', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'draggable', 'itemscope', 'style', 'title', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'lang', 'datetime', 'dir', 'itemref', 'tabindex', 'nonce', 'autocapitalize'}, {'phrasing'}),
        <class 'tuple'>:('title', 'Document title', {'metadata'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'text'}),
        <class 'tuple'>:('tr', 'Table row', {'none'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'script-supporting elements', 'th', 'td'}),
        <class 'tuple'>:('track', 'Timed text track', {'none'}, {'accesskey', 'src', 'hidden', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'draggable', 'srclang', 'itemscope', 'style', 'title', 'enterkeyhint', 'translate', 'contenteditable', 'is', 'inputmode', 'kind', 'lang', 'dir', 'itemref', 'label', 'tabindex', 'default', 'nonce', 'autocapitalize'}, {'empty'}),
        <class 'tuple'>:('u', 'Unarticulated annotation', {'flow', 'phrasing', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('ul', 'List', {'flow', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'li', 'script-supporting elements'}),
        <class 'tuple'>:('var', 'Variable', {'flow', 'phrasing', 'palpable'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'phrasing'}),
        <class 'tuple'>:('video', 'Video player', {'flow', 'phrasing', 'interactive', 'embedded', 'palpable'}, {'accesskey', 'src', 'hidden', 'autoplay', 'itemprop', 'itemtype', 'itemid', 'spellcheck', 'draggable', 'itemscope', 'muted', 'style', 'title', 'enterkeyhint', 'translate', 'crossorigin', 'contenteditable', 'is', 'playsinline', 'inputmode', 'controls', 'loop', 'lang', 'poster', 'width', 'dir', 'itemref', 'tabindex', 'height', 'preload', 'nonce', 'autocapitalize'}, {'source', 'track', 'transparent'}),
        <class 'tuple'>:('wbr', 'Line breaking opportunity', {'flow', 'phrasing'}, {'nonce', 'accesskey', 'itemscope', 'inputmode', 'style', 'dir', 'hidden', 'itemref', 'title', 'itemprop', 'itemtype', 'itemid', 'lang', 'tabindex', 'enterkeyhint', 'spellcheck', 'translate', 'contenteditable', 'autocapitalize', 'draggable', 'is'}, {'empty'})
    ],
    'event_handlers':
    {
        'onabort':
        {
            'applies_to': 'HTML elements'
        },
        'onafterprint':
        {
            'applies_to': 'body'
        },
        'onauxclick':
        {
            'applies_to': 'HTML elements'
        },
        'onbeforeprint':
        {
            'applies_to': 'body'
        },
        'onbeforeunload':
        {
            'applies_to': 'body'
        },
        'onblur':
        {
            'applies_to': 'HTML elements'
        },
        'oncancel':
        {
            'applies_to': 'HTML elements'
        },
        'oncanplay':
        {
            'applies_to': 'HTML elements'
        },
        'oncanplaythrough':
        {
            'applies_to': 'HTML elements'
        },
        'onchange':
        {
            'applies_to': 'HTML elements'
        },
        'onclick':
        {
            'applies_to': 'HTML elements'
        },
        'onclose':
        {
            'applies_to': 'HTML elements'
        },
        'oncontextmenu':
        {
            'applies_to': 'HTML elements'
        },
        'oncopy':
        {
            'applies_to': 'HTML elements'
        },
        'oncuechange':
        {
            'applies_to': 'HTML elements'
        },
        'oncut':
        {
            'applies_to': 'HTML elements'
        },
        'ondblclick':
        {
            'applies_to': 'HTML elements'
        },
        'ondrag':
        {
            'applies_to': 'HTML elements'
        },
        'ondragend':
        {
            'applies_to': 'HTML elements'
        },
        'ondragenter':
        {
            'applies_to': 'HTML elements'
        },
        'ondragexit':
        {
            'applies_to': 'HTML elements'
        },
        'ondragleave':
        {
            'applies_to': 'HTML elements'
        },
        'ondragover':
        {
            'applies_to': 'HTML elements'
        },
        'ondragstart':
        {
            'applies_to': 'HTML elements'
        },
        'ondrop':
        {
            'applies_to': 'HTML elements'
        },
        'ondurationchange':
        {
            'applies_to': 'HTML elements'
        },
        'onemptied':
        {
            'applies_to': 'HTML elements'
        },
        'onended':
        {
            'applies_to': 'HTML elements'
        },
        'onerror':
        {
            'applies_to': 'HTML elements'
        },
        'onfocus':
        {
            'applies_to': 'HTML elements'
        },
        'onformdata':
        {
            'applies_to': 'HTML elements'
        },
        'onhashchange':
        {
            'applies_to': 'body'
        },
        'oninput':
        {
            'applies_to': 'HTML elements'
        },
        'oninvalid':
        {
            'applies_to': 'HTML elements'
        },
        'onkeydown':
        {
            'applies_to': 'HTML elements'
        },
        'onkeypress':
        {
            'applies_to': 'HTML elements'
        },
        'onkeyup':
        {
            'applies_to': 'HTML elements'
        },
        'onlanguagechange':
        {
            'applies_to': 'body'
        },
        'onload':
        {
            'applies_to': 'HTML elements'
        },
        'onloadeddata':
        {
            'applies_to': 'HTML elements'
        },
        'onloadedmetadata':
        {
            'applies_to': 'HTML elements'
        },
        'onloadend':
        {
            'applies_to': 'HTML elements'
        },
        'onloadstart':
        {
            'applies_to': 'HTML elements'
        },
        'onmessage':
        {
            'applies_to': 'body'
        },
        'onmessageerror':
        {
            'applies_to': 'body'
        },
        'onmousedown':
        {
            'applies_to': 'HTML elements'
        },
        'onmouseenter':
        {
            'applies_to': 'HTML elements'
        },
        'onmouseleave':
        {
            'applies_to': 'HTML elements'
        },
        'onmousemove':
        {
            'applies_to': 'HTML elements'
        },
        'onmouseout':
        {
            'applies_to': 'HTML elements'
        },
        'onmouseover':
        {
            'applies_to': 'HTML elements'
        },
        'onmouseup':
        {
            'applies_to': 'HTML elements'
        },
        'onoffline':
        {
            'applies_to': 'body'
        },
        'ononline':
        {
            'applies_to': 'body'
        },
        'onpagehide':
        {
            'applies_to': 'body'
        },
        'onpageshow':
        {
            'applies_to': 'body'
        },
        'onpaste':
        {
            'applies_to': 'HTML elements'
        },
        'onpause':
        {
            'applies_to': 'HTML elements'
        },
        'onplay':
        {
            'applies_to': 'HTML elements'
        },
        'onplaying':
        {
            'applies_to': 'HTML elements'
        },
        'onpopstate':
        {
            'applies_to': 'body'
        },
        'onprogress':
        {
            'applies_to': 'HTML elements'
        },
        'onratechange':
        {
            'applies_to': 'HTML elements'
        },
        'onrejectionhandled':
        {
            'applies_to': 'body'
        },
        'onreset':
        {
            'applies_to': 'HTML elements'
        },
        'onresize':
        {
            'applies_to': 'HTML elements'
        },
        'onscroll':
        {
            'applies_to': 'HTML elements'
        },
        'onsecuritypolicyviolation':
        {
            'applies_to': 'HTML elements'
        },
        'onseeked':
        {
            'applies_to': 'HTML elements'
        },
        'onseeking':
        {
            'applies_to': 'HTML elements'
        },
        'onselect':
        {
            'applies_to': 'HTML elements'
        },
        'onstalled':
        {
            'applies_to': 'HTML elements'
        },
        'onstorage':
        {
            'applies_to': 'body'
        },
        'onsubmit':
        {
            'applies_to': 'HTML elements'
        },
        'onsuspend':
        {
            'applies_to': 'HTML elements'
        },
        'ontimeupdate':
        {
            'applies_to': 'HTML elements'
        },
        'ontoggle':
        {
            'applies_to': 'HTML elements'
        },
        'onunhandledrejection':
        {
            'applies_to': 'body'
        },
        'onunload':
        {
            'applies_to': 'body'
        },
        'onvolumechange':
        {
            'applies_to': 'HTML elements'
        },
        'onwaiting':
        {
            'applies_to': 'HTML elements'
        },
        'onwheel':
        {
            'applies_to': 'HTML elements'
        }
    },
    'input_element_type_attribute_values':
    [
        'button',
        'checkbox',
        'color',
        'date',
        'datetime-local',
        'email',
        'file',
        'hidden',
        'image',
        'month',
        'number',
        'password',
        'radio',
        'range',
        'reset',
        'search',
        'submit',
        'tel',
        'text',
        'time',
        'url',
        'week'
    ]
}
