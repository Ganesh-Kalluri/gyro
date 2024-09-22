/** @leewise-module */

import { SocialPostFormatterMixinBase } from '@social/js/social_post_formatter_mixin';

import { patchWithCleanup } from "@web/../tests/helpers/utils";

QUnit.module('Social Formatter Regex', {}, () => {
    QUnit.test('Facebook Message', (assert) => {
        assert.expect(1);

        patchWithCleanup(SocialPostFormatterMixinBase, {
            _getMediaType() { return 'facebook' },
            _formatPost() {
                this.originalPost = { account_id: { raw_value: 42 } };
                return super._formatPost(...arguments);
            }
        });

        const testMessage = 'Hello @[542132] Leewise-Social, check this out: https://www.leewise.in?utm=mail&param=1 #crazydeals #leewise';
        const finalMessage = SocialPostFormatterMixinBase._formatPost(testMessage);

        assert.equal(finalMessage, [
            "Hello",
            "<a href='/social_facebook/redirect_to_profile/42/542132?name=Leewise-Social' target='_blank'>Leewise-Social</a>,",
            "check this out:",
            "<a href='https://www.leewise.in?utm=mail&amp;param=1' target='_blank' rel='noreferrer noopener'>https://www.leewise.in?utm=mail&amp;param=1</a>",
            "<a href='https://www.facebook.com/hashtag/crazydeals' target='_blank'>#crazydeals</a>",
            "<a href='https://www.facebook.com/hashtag/leewise' target='_blank'>#leewise</a>",
        ].join(' '));
    });

    QUnit.test('Instagram Message', (assert) => {
        assert.expect(1);

        patchWithCleanup(SocialPostFormatterMixinBase, {
            _getMediaType() { return 'instagram' },
        });

        const testMessage = 'Hello @Leewise.Social, check this out: https://www.leewise.in #crazydeals #leewise';
        const finalMessage = SocialPostFormatterMixinBase._formatPost(testMessage);

        assert.equal(finalMessage, [
            "Hello",
            "<a href='https://www.instagram.com/Leewise.Social' target='_blank'>@Leewise.Social</a>,",
            "check this out:",
            "<a href='https://www.leewise.in' target='_blank' rel='noreferrer noopener'>https://www.leewise.in</a>",
            "<a href='https://www.instagram.com/explore/tags/crazydeals' target='_blank'>#crazydeals</a>",
            "<a href='https://www.instagram.com/explore/tags/leewise' target='_blank'>#leewise</a>",
        ].join(' '));
    });

    QUnit.test('LinkedIn Message', (assert) => {
        assert.expect(1);

        patchWithCleanup(SocialPostFormatterMixinBase, {
            _getMediaType() { return 'linkedin' },
        });

        const testMessage = 'Hello, check this out: https://www.leewise.in {hashtag|#|crazydeals} #leewise';
        const finalMessage = SocialPostFormatterMixinBase._formatPost(testMessage);

        assert.equal(finalMessage, [
            "Hello, check this out:",
            "<a href='https://www.leewise.in' target='_blank' rel='noreferrer noopener'>https://www.leewise.in</a>",
            "<a href='https://www.linkedin.com/feed/hashtag/crazydeals' target='_blank'>#crazydeals</a>",
            "<a href='https://www.linkedin.com/feed/hashtag/leewise' target='_blank'>#leewise</a>",
        ].join(' '));
    });

    QUnit.test('Twitter Message', (assert) => {
        assert.expect(1);

        patchWithCleanup(SocialPostFormatterMixinBase, {
            _getMediaType() { return 'twitter' },
        });

        const testMessage = 'Hello @Leewise-Social, check this out: https://www.leewise.in #crazydeals #leewise';
        const finalMessage = SocialPostFormatterMixinBase._formatPost(testMessage);

        assert.equal(finalMessage, [
            "Hello",
            "<a href='https://twitter.com/Leewise-Social' target='_blank'>@Leewise-Social</a>,",
            "check this out:",
            "<a href='https://www.leewise.in' target='_blank' rel='noreferrer noopener'>https://www.leewise.in</a>",
            "<a href='https://twitter.com/hashtag/crazydeals?src=hash' target='_blank'>#crazydeals</a>",
            "<a href='https://twitter.com/hashtag/leewise?src=hash' target='_blank'>#leewise</a>",
        ].join(' '));
    });

    QUnit.test('YouTube Message', (assert) => {
        assert.expect(1);

        patchWithCleanup(SocialPostFormatterMixinBase, {
            _getMediaType() { return 'youtube' },
        });

        const testMessage = 'Hello, check this out: https://www.leewise.in #crazydeals #leewise';
        const finalMessage = SocialPostFormatterMixinBase._formatPost(testMessage);

        assert.equal(finalMessage, [
            "Hello, check this out:",
            "<a href='https://www.leewise.in' target='_blank' rel='noreferrer noopener'>https://www.leewise.in</a>",
            "<a href='https://www.youtube.com/results?search_query=%23crazydeals' target='_blank'>#crazydeals</a>",
            "<a href='https://www.youtube.com/results?search_query=%23leewise' target='_blank'>#leewise</a>",
        ].join(' '));
    });
});
