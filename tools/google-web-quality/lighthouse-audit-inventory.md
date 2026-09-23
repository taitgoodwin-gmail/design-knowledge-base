# Lighthouse 13.5.0 audit inventory

Checked: 23 September 2026.

Extracted **165 category references covering 162 unique audit IDs** from the [pinned default configuration](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/config/default-config.js). Each audit ID was resolved to a source file. This is a source inventory, not website test results.

Weights below are configured inputs, not final percentages. Runtime mode, applicability and errors affect inclusion and scoring. Zero weight does not mean unimportant. Shared checks must not be counted twice as customer issues. Experimental agentic checks require separate interpretation.

| Category | References |
| --- | ---: |
| performance | 50 |
| accessibility | 76 |
| best-practices | 21 |
| seo | 11 |
| agentic-browsing | 7 |

## performance

| Audit ID and implementation | Configured weight | Group | Role |
| --- | ---: | --- | --- |
| [first-contentful-paint](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/metrics/first-contentful-paint.js) | 10 | metrics | weighted reference |
| [largest-contentful-paint](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/metrics/largest-contentful-paint.js) | 25 | metrics | weighted reference |
| [total-blocking-time](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/metrics/total-blocking-time.js) | 30 | metrics | weighted reference |
| [cumulative-layout-shift](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/metrics/cumulative-layout-shift.js) | 25 | metrics | weighted reference |
| [speed-index](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/metrics/speed-index.js) | 10 | metrics | weighted reference |
| [interaction-to-next-paint](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/metrics/interaction-to-next-paint.js) | 0 | metrics | unscored reference |
| [cache-insight](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/insights/cache-insight.js) | 0 | insights | unscored reference |
| [cls-culprits-insight](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/insights/cls-culprits-insight.js) | 0 | insights | unscored reference |
| [document-latency-insight](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/insights/document-latency-insight.js) | 0 | insights | unscored reference |
| [dom-size-insight](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/insights/dom-size-insight.js) | 0 | insights | unscored reference |
| [duplicated-javascript-insight](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/insights/duplicated-javascript-insight.js) | 0 | insights | unscored reference |
| [font-display-insight](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/insights/font-display-insight.js) | 0 | insights | unscored reference |
| [forced-reflow-insight](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/insights/forced-reflow-insight.js) | 0 | insights | unscored reference |
| [image-delivery-insight](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/insights/image-delivery-insight.js) | 0 | insights | unscored reference |
| [inp-breakdown-insight](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/insights/inp-breakdown-insight.js) | 0 | insights | unscored reference |
| [lcp-breakdown-insight](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/insights/lcp-breakdown-insight.js) | 0 | insights | unscored reference |
| [lcp-discovery-insight](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/insights/lcp-discovery-insight.js) | 0 | insights | unscored reference |
| [legacy-javascript-insight](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/insights/legacy-javascript-insight.js) | 0 | insights | unscored reference |
| [modern-http-insight](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/insights/modern-http-insight.js) | 0 | insights | unscored reference |
| [network-dependency-tree-insight](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/insights/network-dependency-tree-insight.js) | 0 | insights | unscored reference |
| [render-blocking-insight](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/insights/render-blocking-insight.js) | 0 | insights | unscored reference |
| [third-parties-insight](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/insights/third-parties-insight.js) | 0 | insights | unscored reference |
| [viewport-insight](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/insights/viewport-insight.js) | 0 | insights | unscored reference |
| [interactive](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/metrics/interactive.js) | 0 | hidden | unscored reference |
| [max-potential-fid](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/metrics/max-potential-fid.js) | 0 | hidden | unscored reference |
| [unminified-css](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/byte-efficiency/unminified-css.js) | 0 | diagnostics | unscored reference |
| [unminified-javascript](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/byte-efficiency/unminified-javascript.js) | 0 | diagnostics | unscored reference |
| [unused-css-rules](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/byte-efficiency/unused-css-rules.js) | 0 | diagnostics | unscored reference |
| [unused-javascript](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/byte-efficiency/unused-javascript.js) | 0 | diagnostics | unscored reference |
| [total-byte-weight](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/byte-efficiency/total-byte-weight.js) | 0 | diagnostics | unscored reference |
| [user-timings](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/user-timings.js) | 0 | diagnostics | unscored reference |
| [bootup-time](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/bootup-time.js) | 0 | diagnostics | unscored reference |
| [mainthread-work-breakdown](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/mainthread-work-breakdown.js) | 0 | diagnostics | unscored reference |
| [long-tasks](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/long-tasks.js) | 0 | diagnostics | unscored reference |
| [non-composited-animations](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/non-composited-animations.js) | 0 | diagnostics | unscored reference |
| [unsized-images](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/unsized-images.js) | 0 | diagnostics | unscored reference |
| [bf-cache](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/bf-cache.js) | 0 | diagnostics | unscored reference |
| [network-requests](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/network-requests.js) | 0 | hidden | unscored reference |
| [network-rtt](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/network-rtt.js) | 0 | hidden | unscored reference |
| [network-server-latency](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/network-server-latency.js) | 0 | hidden | unscored reference |
| [main-thread-tasks](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/main-thread-tasks.js) | 0 | hidden | unscored reference |
| [diagnostics](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/diagnostics.js) | 0 | hidden | unscored reference |
| [metrics](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/metrics.js) | 0 | hidden | unscored reference |
| [screenshot-thumbnails](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/screenshot-thumbnails.js) | 0 | hidden | unscored reference |
| [final-screenshot](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/final-screenshot.js) | 0 | hidden | unscored reference |
| [script-treemap-data](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/script-treemap-data.js) | 0 | hidden | unscored reference |
| [resource-summary](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/resource-summary.js) | 0 | hidden | unscored reference |
| [redirects](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/redirects.js) | 0 | hidden | unscored reference |
| [server-response-time](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/server-response-time.js) | 0 | hidden | unscored reference |
| [layout-shifts](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/layout-shifts.js) | 0 | hidden | unscored reference |

## accessibility

| Audit ID and implementation | Configured weight | Group | Role |
| --- | ---: | --- | --- |
| [accesskeys](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/accesskeys.js) | 7 | a11y-navigation | weighted reference |
| [aria-allowed-attr](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/aria-allowed-attr.js) | 10 | a11y-aria | weighted reference |
| [aria-command-name](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/aria-command-name.js) | 7 | a11y-aria | weighted reference |
| [aria-conditional-attr](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/aria-conditional-attr.js) | 7 | a11y-aria | weighted reference |
| [aria-deprecated-role](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/aria-deprecated-role.js) | 1 | a11y-aria | weighted reference |
| [aria-dialog-name](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/aria-dialog-name.js) | 7 | a11y-aria | weighted reference |
| [aria-hidden-body](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/aria-hidden-body.js) | 10 | a11y-aria | weighted reference |
| [aria-hidden-focus](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/aria-hidden-focus.js) | 7 | a11y-aria | weighted reference |
| [aria-input-field-name](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/aria-input-field-name.js) | 7 | a11y-aria | weighted reference |
| [aria-meter-name](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/aria-meter-name.js) | 7 | a11y-aria | weighted reference |
| [aria-progressbar-name](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/aria-progressbar-name.js) | 7 | a11y-aria | weighted reference |
| [aria-prohibited-attr](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/aria-prohibited-attr.js) | 7 | a11y-aria | weighted reference |
| [aria-required-attr](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/aria-required-attr.js) | 10 | a11y-aria | weighted reference |
| [aria-required-children](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/aria-required-children.js) | 10 | a11y-aria | weighted reference |
| [aria-required-parent](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/aria-required-parent.js) | 10 | a11y-aria | weighted reference |
| [aria-roles](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/aria-roles.js) | 10 | a11y-aria | weighted reference |
| [aria-text](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/aria-text.js) | 7 | a11y-aria | weighted reference |
| [aria-toggle-field-name](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/aria-toggle-field-name.js) | 7 | a11y-aria | weighted reference |
| [aria-tooltip-name](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/aria-tooltip-name.js) | 7 | a11y-aria | weighted reference |
| [aria-treeitem-name](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/aria-treeitem-name.js) | 7 | a11y-aria | weighted reference |
| [aria-valid-attr-value](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/aria-valid-attr-value.js) | 10 | a11y-aria | weighted reference |
| [aria-valid-attr](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/aria-valid-attr.js) | 10 | a11y-aria | weighted reference |
| [button-name](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/button-name.js) | 10 | a11y-names-labels | weighted reference |
| [bypass](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/bypass.js) | 7 | a11y-navigation | weighted reference |
| [color-contrast](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/color-contrast.js) | 7 | a11y-color-contrast | weighted reference |
| [definition-list](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/definition-list.js) | 7 | a11y-tables-lists | weighted reference |
| [dlitem](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/dlitem.js) | 7 | a11y-tables-lists | weighted reference |
| [document-title](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/document-title.js) | 7 | a11y-names-labels | weighted reference |
| [duplicate-id-aria](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/duplicate-id-aria.js) | 10 | a11y-aria | weighted reference |
| [form-field-multiple-labels](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/form-field-multiple-labels.js) | 3 | a11y-names-labels | weighted reference |
| [frame-title](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/frame-title.js) | 7 | a11y-names-labels | weighted reference |
| [heading-order](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/heading-order.js) | 3 | a11y-navigation | weighted reference |
| [html-has-lang](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/html-has-lang.js) | 7 | a11y-language | weighted reference |
| [html-lang-valid](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/html-lang-valid.js) | 7 | a11y-language | weighted reference |
| [html-xml-lang-mismatch](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/html-xml-lang-mismatch.js) | 3 | a11y-language | weighted reference |
| [image-alt](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/image-alt.js) | 10 | a11y-names-labels | weighted reference |
| [input-button-name](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/input-button-name.js) | 10 | a11y-names-labels | weighted reference |
| [input-image-alt](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/input-image-alt.js) | 10 | a11y-names-labels | weighted reference |
| [label](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/label.js) | 10 | a11y-names-labels | weighted reference |
| [link-in-text-block](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/link-in-text-block.js) | 7 | a11y-color-contrast | weighted reference |
| [link-name](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/link-name.js) | 7 | a11y-names-labels | weighted reference |
| [list](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/list.js) | 7 | a11y-tables-lists | weighted reference |
| [listitem](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/listitem.js) | 7 | a11y-tables-lists | weighted reference |
| [meta-refresh](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/meta-refresh.js) | 10 | a11y-best-practices | weighted reference |
| [meta-viewport](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/meta-viewport.js) | 10 | a11y-best-practices | weighted reference |
| [object-alt](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/object-alt.js) | 7 | a11y-names-labels | weighted reference |
| [select-name](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/select-name.js) | 10 | a11y-names-labels | weighted reference |
| [skip-link](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/skip-link.js) | 3 | a11y-names-labels | weighted reference |
| [tabindex](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/tabindex.js) | 7 | a11y-navigation | weighted reference |
| [target-size](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/target-size.js) | 7 | a11y-best-practices | weighted reference |
| [td-headers-attr](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/td-headers-attr.js) | 7 | a11y-tables-lists | weighted reference |
| [th-has-data-cells](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/th-has-data-cells.js) | 7 | a11y-tables-lists | weighted reference |
| [valid-lang](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/valid-lang.js) | 7 | a11y-language | weighted reference |
| [video-caption](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/video-caption.js) | 10 | a11y-audio-video | weighted reference |
| [landmark-one-main](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/landmark-one-main.js) | 3 | a11y-best-practices | weighted reference |
| [autocomplete-valid](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/autocomplete-valid.js) | 1 | a11y-best-practices | weighted reference |
| [presentation-role-conflict](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/presentation-role-conflict.js) | 1 | a11y-best-practices | weighted reference |
| [svg-img-alt](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/svg-img-alt.js) | 1 | a11y-best-practices | weighted reference |
| [focusable-controls](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/manual/focusable-controls.js) | 0 | — | manual review |
| [interactive-element-affordance](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/manual/interactive-element-affordance.js) | 0 | — | manual review |
| [logical-tab-order](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/manual/logical-tab-order.js) | 0 | — | manual review |
| [visual-order-follows-dom](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/manual/visual-order-follows-dom.js) | 0 | — | manual review |
| [focus-traps](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/manual/focus-traps.js) | 0 | — | manual review |
| [managed-focus](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/manual/managed-focus.js) | 0 | — | manual review |
| [use-landmarks](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/manual/use-landmarks.js) | 0 | — | manual review |
| [offscreen-content-hidden](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/manual/offscreen-content-hidden.js) | 0 | — | manual review |
| [custom-controls-labels](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/manual/custom-controls-labels.js) | 0 | — | manual review |
| [custom-controls-roles](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/manual/custom-controls-roles.js) | 0 | — | manual review |
| [table-duplicate-name](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/table-duplicate-name.js) | 0 | a11y-best-practices | unscored reference |
| [empty-heading](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/empty-heading.js) | 0 | a11y-best-practices | unscored reference |
| [aria-allowed-role](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/aria-allowed-role.js) | 0 | a11y-best-practices | unscored reference |
| [image-redundant-alt](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/image-redundant-alt.js) | 0 | a11y-names-labels | unscored reference |
| [identical-links-same-purpose](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/identical-links-same-purpose.js) | 0 | a11y-best-practices | unscored reference |
| [label-content-name-mismatch](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/label-content-name-mismatch.js) | 0 | hidden | unscored reference |
| [table-fake-caption](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/table-fake-caption.js) | 0 | hidden | unscored reference |
| [td-has-header](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/td-has-header.js) | 0 | hidden | unscored reference |

## best-practices

| Audit ID and implementation | Configured weight | Group | Role |
| --- | ---: | --- | --- |
| [is-on-https](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/is-on-https.js) | 5 | best-practices-trust-safety | weighted reference |
| [redirects-http](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/redirects-http.js) | 1 | best-practices-trust-safety | weighted reference |
| [geolocation-on-start](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/dobetterweb/geolocation-on-start.js) | 1 | best-practices-trust-safety | weighted reference |
| [notification-on-start](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/dobetterweb/notification-on-start.js) | 1 | best-practices-trust-safety | weighted reference |
| [csp-xss](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/csp-xss.js) | 0 | best-practices-trust-safety | unscored reference |
| [has-hsts](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/has-hsts.js) | 0 | best-practices-trust-safety | unscored reference |
| [origin-isolation](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/origin-isolation.js) | 0 | best-practices-trust-safety | unscored reference |
| [clickjacking-mitigation](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/clickjacking-mitigation.js) | 0 | best-practices-trust-safety | unscored reference |
| [trusted-types-xss](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/trusted-types-xss.js) | 0 | best-practices-trust-safety | unscored reference |
| [paste-preventing-inputs](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/dobetterweb/paste-preventing-inputs.js) | 3 | best-practices-ux | weighted reference |
| [image-aspect-ratio](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/image-aspect-ratio.js) | 1 | best-practices-ux | weighted reference |
| [image-size-responsive](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/image-size-responsive.js) | 1 | best-practices-ux | weighted reference |
| [doctype](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/dobetterweb/doctype.js) | 1 | best-practices-browser-compat | weighted reference |
| [charset](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/dobetterweb/charset.js) | 1 | best-practices-browser-compat | weighted reference |
| [baseline](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/baseline.js) | 0 | best-practices-browser-compat | unscored reference |
| [js-libraries](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/dobetterweb/js-libraries.js) | 0 | best-practices-general | unscored reference |
| [deprecations](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/deprecations.js) | 5 | best-practices-general | weighted reference |
| [third-party-cookies](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/third-party-cookies.js) | 5 | best-practices-general | weighted reference |
| [errors-in-console](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/errors-in-console.js) | 1 | best-practices-general | weighted reference |
| [valid-source-maps](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/valid-source-maps.js) | 0 | best-practices-general | unscored reference |
| [inspector-issues](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/dobetterweb/inspector-issues.js) | 1 | best-practices-general | weighted reference |

## seo

| Audit ID and implementation | Configured weight | Group | Role |
| --- | ---: | --- | --- |
| [is-crawlable](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/seo/is-crawlable.js) | 93 / 23 | seo-crawl | weighted reference |
| [document-title](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/document-title.js) | 1 | seo-content | weighted reference |
| [meta-description](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/seo/meta-description.js) | 1 | seo-content | weighted reference |
| [http-status-code](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/seo/http-status-code.js) | 1 | seo-crawl | weighted reference |
| [link-text](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/seo/link-text.js) | 1 | seo-content | weighted reference |
| [crawlable-anchors](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/seo/crawlable-anchors.js) | 1 | seo-crawl | weighted reference |
| [robots-txt](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/seo/robots-txt.js) | 1 | seo-crawl | weighted reference |
| [image-alt](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/accessibility/image-alt.js) | 1 | seo-content | weighted reference |
| [hreflang](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/seo/hreflang.js) | 1 | seo-content | weighted reference |
| [canonical](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/seo/canonical.js) | 1 | seo-content | weighted reference |
| [structured-data](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/seo/manual/structured-data.js) | 0 | — | manual review |

## agentic-browsing

| Audit ID and implementation | Configured weight | Group | Role |
| --- | ---: | --- | --- |
| [agent-accessibility-tree](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/agentic/agent-accessibility-tree.js) | 1 | agent-accessibility | weighted reference |
| [webmcp-form-coverage](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/webmcp-form-coverage.js) | 1 | webmcp | weighted reference |
| [webmcp-registered-tools](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/webmcp-registered-tools.js) | 1 | webmcp | weighted reference |
| [webmcp-schema-validity](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/webmcp-schema-validity.js) | 1 | webmcp | weighted reference |
| [cumulative-layout-shift](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/metrics/cumulative-layout-shift.js) | 1 | — | weighted reference |
| [llms-txt](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/agentic/llms-txt.js) | 1 | agent-discoverability | weighted reference |
| [ard-schema](https://github.com/GoogleChrome/lighthouse/blob/cb853a38a6410617518b363590c967b3fe211949/core/audits/agentic/ard-schema.js) | 1 | agent-discoverability | weighted reference |

## Verification

Source commit: `cb853a38a6410617518b363590c967b3fe211949`. Extraction asserted that every reference maps to exactly one audit source file. JSON contains the same records for future import. Titles, availability and results should be taken from each actual Lighthouse report; this inventory must be regenerated after version upgrades.
